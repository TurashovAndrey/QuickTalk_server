import tornado.web
import simplejson
from helpers.helper_functions import *
from models.user_model import UserModel
from models.database_structure import *
import uuid
import arrow
import bcrypt


class SignUpHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            response = dict()
            user = dict()

            username = get_json_argument(self.request.body, 'username', None)
            password = get_json_argument(self.request.body,'password', None)
            email = u"test@test.com"
            first_name = ""
            last_name = ""
            telephone = ""

            if email is None or password is None:
                raise Exception('Need username, password to create user.')

            if len(password) < 8:
                raise Exception('Password must be greater than 8 symbols')

            u = UserModel().get_user(email=email)
            if isinstance(u, UserModel) and u.user_id is not None:
                raise Exception('User with email %s already exists' % email)

            user_id = uuid.uuid4()
            created = arrow.utcnow().timestamp

            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(11))
            hashed = unicode(hashed)

            user['user_id'] = user_id
            user['username'] = username
            user['hashed_pw'] = hashed
            user['first_name'] = first_name
            user['last_name'] = last_name
            user['email'] = email
            user['created'] = created
            user['updated'] = created
            user['telephone'] = telephone

            UserModel().create_user(**user)
        except Exception, e:
            pass