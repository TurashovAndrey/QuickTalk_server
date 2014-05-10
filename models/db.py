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
        #self._pg_database = create_database("postgres://%s:%s@%s/%s?isolation=read-committed" % (
        #    options.postgresql_user, options.postgresql_pass,
        #    options.postgresql_host, options.postgresql_db)
        #)
        self.database = create_database("postgres://%s:%s@%s/%s?isolation=read-committed" % (
                "leasing", "1234567","127.0.0.1", "leasing_db")
        )
        _store = Store(self.database)
        return _store

    def fetchAll(self, rows):
        data = list()
        for r in rows:
            d = {}
            for prop in dir(r):
                if prop[0] != '_':
                    d[prop] = getattr(r, prop)

            if len(d.keys()) > 0:
                data.append(d)

        return data
