from storm.locals import *

class Database():
    def __init__(self):
        self.database = create_database("postgres://%s:%s@%s/%s?isolation=read-committed" % (
                        "leasing", "1234567","127.0.0.1", "leasing_db")
                    )
        self.store = Store(self.database)
