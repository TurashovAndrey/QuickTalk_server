import tornado.web
import simplejson
from helpers.helper_functions import *
from models.user_model import UserModel
from models.database_structure import *


class SignUpHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            response = dict()
            user = dict()

            args = simplejson.loads(self.request.body)
            email = get_json_argument('email', None)
            password = get_json_argument('password', None)

            if email is None or password is None:
                raise Exception('Need username, password to create user.')

            if len(password) < 8:
                raise Exception('Password must be greater than 8 symbols')

            u = UserModel().get_user(email=email)
            if isinstance(u, User) and u.user_id is not None:
                raise Exception('User with email %s already exists' % email)

        except Exception, e:
            self.write_exception(e)
            self.finish()
