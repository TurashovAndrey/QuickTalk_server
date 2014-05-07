import tornado.web
from models.database_structure import User
from models.db import Database
import simplejson

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        db = Database()
        res = db.store.find(User)
        r = list(res)
        self.write("Hello, world")