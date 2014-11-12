from storm.locals import *
from tornado.options import options
import storm.database

class Database():

    store = None
    def __init__(self, _store=None):
        if _store is not None:
           Database.store = _store
        else:
            if Database.store is None:
                Database.store = self.getDB()

    def getDB(self):
        self.database = create_database("postgres://%s:%s@%s/%s?isolation=read-committed" % (
                options.db_user, options.db_password, options.db_host, options.db_name)
        )
        _store = Store(self.database)
        return _store
