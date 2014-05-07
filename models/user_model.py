from database_structure import User
from DB import *

class UserModel():
    def get_user(self, email):
        db = Database()
        user = db.store.find(User, User.email == email).first()
        return user
