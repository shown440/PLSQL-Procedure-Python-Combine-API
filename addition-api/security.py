from werkzeug.security import safe_str_cmp

from models.user import UserModel

# authenticate_user = ""
def authenticate(username, password):   # service_id, , service_id
    pran_rfl_serviceId = "2"

    #print("******", service_id,"****", username)

    #serid = service_id
    #serid = UserModel.find_by_serid(service_id, username, password)
    user = UserModel.find_by_username(username) #, service_id
    my_password = UserModel.encrypt_password(password)
    # print(type(user.username))
    # print(user.serid)
    # print(type((user.serid)))
    
    if (user.serid==pran_rfl_serviceId) and user and safe_str_cmp(user.password, my_password):
        #print(user.password)
        return user
#authenticate("bob","asdf")

def identity(payload):
    user_id = payload["identity"]
    #print(user_id)
    return UserModel.find_by_id(user_id)   #user_id
#identity(payload)

