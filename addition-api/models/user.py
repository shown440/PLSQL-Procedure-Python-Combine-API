import hashlib

import cx_Oracle

from db import db

#####################################################
##### Finding User Class ############################
#####################################################
class UserModel(db.Model):
    __tablename__ = "TANPOOL_AUTH"  # SHIFULLAH.
    __table_args__ = {'extend_existing': True}  # 'schema': 'SHIFULLAH', 

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(500))
    serid = db.Column(db.String(100))

    def __init__(self, id, username, password, serid):
        self.id = id
        self.username = username
        self.password = password
        self.serid = serid

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_username_serviceid(cls, username, service_id):
        return cls.query.filter_by(username=username, serid=service_id).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encrypt_password(cls, encryption_desire_password):
        encrypted_pass_str = hashlib.sha512(encryption_desire_password.encode()).hexdigest()
        return encrypted_pass_str   #cls.query.filter_by(id=_id).first()
