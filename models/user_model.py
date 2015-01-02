from database_structure import User
from db import *
import uuid
import bcrypt

class UserModel(Database):
    def get_user(self, email=None, user_id=None ):
        if email:
            user = self.store.find(User, User.email == email).one()
        elif user_id:
            user = self.store.find(User, User.user_id == user_id).one()

        return user

    def create_user(self, **kw):
        u = User()
        u.user_id = kw['user_id']
        u.hashed_pw = kw['hashed_pw']
        u.email = kw['email']
        u.created = kw['created']
        u.updated = kw['updated']

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

    def check_password(self, email, password):
        users = self.store.find(User, User.email.lower() == email.lower())
        for user in users:
            if bcrypt.hashpw(password.encode('utf-8'), user.hashed_pw.encode('utf-8')) == user.hashed_pw:
                return user

        return None

    def get_users(self):
        return self.store.find(User, User.email == email)
