from storm.locals import *

class User(object):
   __storm_table__ = "leasing_users"
   id = Int(primary=True)
   email = Unicode()
