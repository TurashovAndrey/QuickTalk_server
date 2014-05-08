from database_structure import User
from db import *
import uuid

class UserModel():
    def get_user(self, email):
        db = Database()
        user = db.store.find(User, User.email == email).one()
        return user

    def create_user(self, **kw):
        db = Database()

        #kw['user_id'] = uuid.UUID(kw['user_id'])
        u = User()
        u.user_id = kw['user_id']
        u.username = unicode(kw['username'])
        u.hashed_pw = kw['hashed_pw']
        #if 'first_name' in kw.keys():
        #    u.first_name = kw['first_name']
        #if 'last_name' in kw.keys():
        #    u.last_name = kw['last_name']
        #u.email = kw['email']
        #u.created = kw['created']
        #u.created_ip = kw['created_ip']
        #u.updated = kw['updated']
        #u.updated_ip = kw['updated_ip']
        #u.telephone = kw['telephone']
        #
        #if 'gender' in kw.keys():
        #    u.gender = kw['gender']

        #u.is_active = True
        #u.is_deleted = False

        db.store.add(u)

        db.store.commit()
