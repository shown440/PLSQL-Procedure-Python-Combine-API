from db import db

from models.user import UserModel

from flask_restful import Resource, reqparse

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


pran_rfl_serviceId = "2"
###############################################################
###### User Register/ Signup Class ############################
###############################################################
class UserRegister(Resource):
    ##############################################################
    ########### Signin to Oracle DB part ########################
    ##############################################################
    parser = reqparse.RequestParser()

    parser.add_argument("service-id",
        type = str,
        required = True,
        help = "Service ID cannot be blank."
    )
    parser.add_argument("username",
        type = str,
        required = True,
        help = "User name cannot be blank."
    )
    parser.add_argument("password",
        type = str,
        required = True,
        help = "Password cannot be blank."
    )

    @jwt_required()
    def post(self):     #, id

        data = UserRegister.parser.parse_args()
        if data["service-id"] == pran_rfl_serviceId:

            username = data["username"]
            service_id = data["service-id"]
            password = data["password"]
            encrypted_password = UserModel.encrypt_password(password)

            ### Check Admin or not #####
            admin_user = "shown440"
            authenticated_username = current_identity.username
            if safe_str_cmp(authenticated_username, admin_user) != True:
                return {"message":"Only Admin can create user."}, 400

            if UserModel.find_by_username_serviceid(username, service_id):
                return {"message":"{} is already exist in service-id {}.".format(username, service_id)}, 400

            sql = db.text('SELECT (NVL(MAX(ID),0)+1) FROM TANPOOL_AUTH')
            user_master_id = db.engine.execute(sql).fetchone()

            user = UserModel(user_master_id[0], data["username"], encrypted_password, data["service-id"]) # UserModel(data["id"], data["username"], data["password"]) = UserModel(**data)
            user.save_to_db()

            return {"message":"{} is created successfully as your authentication user".format(data["username"])}, 201
        else:
            return {"message":"Service ID is unknown"}


###############################################################
###### User Password update Class ############################
###############################################################
class UserUpdate(Resource):
    ##############################################################
    ########### Signin to Oracle DB part ########################
    ##############################################################
    
    ############################################################################
    ### Working for PUT of user password update. (Date: 28-11-2019) 
    ############################################################################
    parser = reqparse.RequestParser()

    parser.add_argument("service-id",
        type = str,
        required = True,
        help = "Service ID cannot be blank."
    )
    parser.add_argument("username",
        type = str,
        required = True,
        help = "User name cannot be blank."
    )
    parser.add_argument("current-password",
        type = str,
        required = True,
        help = "Current password cannot be blank."
    )
    parser.add_argument("type-new-password",
        type = str,
        required = True,
        help = "New Password cannot be blank."
    )
    parser.add_argument("re-type-new-password",
        type = str,
        required = True,
        help = "New Password cannot be blank."
    )

    @jwt_required()
    def put(self):  #, id

        data = UserUpdate.parser.parse_args()
        if data["service-id"] == pran_rfl_serviceId:

            username = data["username"]
            service_id = data["service-id"]
            current_password = data["current-password"]
            encrypted_current_password = UserModel.encrypt_password(current_password)

            type_new_password = data["type-new-password"]
            re_type_new_password = data["re-type-new-password"]
            encrypted_password = UserModel.encrypt_password(type_new_password)

            #### nijer password nije sara onno kew change korte parbe na ######
            authenticated_username = current_identity.username
            if safe_str_cmp(authenticated_username, username) != True:
                return {"message":"{}, you unauthorised for this update.".format(authenticated_username)}, 400

            if UserModel.find_by_username_serviceid(username, service_id):
                user = UserModel.find_by_username(username)
                if safe_str_cmp(user.password, encrypted_current_password) != True:
                    return {"message":"{}, you entered wrong password.".format(username)}, 400
                if (len(type_new_password)<1) or (len(re_type_new_password)<1):
                    return {"message":"{}, your both of new password cannot be empty.".format(username)}, 400
                if (safe_str_cmp(type_new_password, re_type_new_password) != True):
                    return {"message":"{}, your both of new password have to match.".format(username)}, 400

                user = UserModel.find_by_username_serviceid(username, service_id)
                user.password = encrypted_password
                user.save_to_db()
                return {"message":"{} is successfully updated password.".format(data["username"])}, 201

            return {"message":"{} does not exist with service-id {}.".format(username, service_id)}, 400
        else:
            return {"message":"Service ID is unknown"}


