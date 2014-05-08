from storm.locals import *

class User(object):
    __storm_table__ = "leasing_user"
    id = Int(primary=True)
    user_id = UUID()
    username = Unicode()
    hashed_pw = Unicode()
    first_name = Unicode()
    last_name = Unicode()
    email = Unicode()
    created = Int()
    created_ip = Unicode()
    updated = Int()
    updated_ip = Unicode()
    birthday = Date()
    hometown = Unicode()