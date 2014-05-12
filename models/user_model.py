from database_structure import User
from db import *
import uuid
import bcrypt

class UserModel(Database):
    def get_user(self, email):
        user = self.store.find(User, User.email == email).one()
        return user

    def create_user(self, **kw):
        #kw['user_id'] = uuid.UUID(kw['user_id'])

        u = User()
        u.user_id = kw['user_id']
        u.username = unicode(kw['username'])
        u.hashed_pw = kw['hashed_pw']
        if 'first_name' in kw.keys():
            u.first_name = kw['first_name']
        if 'last_name' in kw.keys():
            u.last_name = kw['last_name']
        u.email = kw['email']
        u.created_ip = kw['created_ip']
        u.updated_ip = kw['updated_ip']
        u.telephone = kw['telephone']

        u.is_active = True
        u.is_deleted = False

        self.store.add(u)

        self.store.commit()

    def update_user(self, **kw):
        user = self.store.find(User, User.user_id == kw['user_id'])

        if user:
            user.set(**kw)

        self.store.commit()

    def delete(self, **kw):
        user = self.store.find(User, User.user_id == kw['user_id'])

        if user:
            user.is_deleted = True

        self.store.commit

    def check_password(self, username, password):
        users = self.store.find(User, User.username.lower() == username.lower())
        for user in users:
            if bcrypt.hashpw(password.encode('utf-8'), user.hashed_pw.encode('utf-8')) == user.hashed_pw:
                return user

        return None
