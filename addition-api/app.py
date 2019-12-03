from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import cx_Oracle

from security import authenticate, identity
from resources.user import UserRegister, UserUpdate
# from resources.item import Item, ItemList
from resources.store import StoreList

# Import socket for get ip dynamically
# import socket

# from db import db
app = Flask(__name__)

# Database Connectivity
app.config["SQLALCHEMY_DATABASE_URI"] = 'oracle+cx_oracle://shifullah:shifullah@10.11.201.251:1521/stlbas'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'oracle+cx_oracle://stlbas:stlbas@10.11.201.251:1521/stlbas'

# app.config["SQLALCHEMY_DATABASE_URI"] = 'oracle+cx_oracle://shifullah:shifullah@10.11.201.55:1525/?service_name=testpdb'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# its turn off the flask-sqlalchemy modification tracker but don't turn off SQLAlchemy modification tracker
app.secret_key = "shifullah_ahmed_khan"
api = Api(app)

# This part should be run under the 'run.py' file
from db import db
db.init_app(app)
@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_AUTH_URL_RULE'] = '/api/v1/transactions/2/auth'
jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(StoreList, "/api/v1/transactions/<int:id>/<int:a>/<int:b>")
# api.add_resource(Store, "/api/v1/transactions/<int:id>/<string:todate>/<string:fromdate>")
# api.add_resource(UserRegister, "/auth/")
# api.add_resource(UserRegister, "/api/v1/transactions/2/register/")
api.add_resource(UserUpdate, "/api/v1/transactions/2/update/")


# ##################### GET IP Address Dynamically #################
# hostname = socket.gethostname()
# IP_address = socket.gethostbyname(hostname)

if __name__ == '__main__':
    # from db import db
    # db.init_app(app)
    app.debug=True
    app.run(host="127.0.0.1" , port='5500')   # host="10.11.200.39", IP_address , port='5000'
