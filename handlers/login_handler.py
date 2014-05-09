from base_handler import BaseHandler
from helpers.helper_functions import *
from models.user_model import UserModel
from models.database_structure import *
import uuid
import arrow
import bcrypt
from helpers.session import Session


class SignUpHandler(BaseHandler):
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

class LoginHandler(BaseHandler):
    def post(self):
        try:
            response = dict()
            username = get_json_argument(self.request.body, "username", None)
            password = get_json_argument(self.request.body, "password", None)

            if username is None or password is None:
                raise Exception(u"You must supply a username and password.")

            user = UserModel().check_password(username, password)
            if user is None:
                raise Exception(u"Invalid username or password!")

            sid = self.session.sessionid
            session = Session(self.application.session_store, sid)
            session['username'] = user.username
            session['user_id'] = user.user_id
            session['first_name'] = user.first_name
            session['last_name'] = user.last_name
            self.set_secure_cookie('sid', sid, expires_days=30, domain="test.com")
            response['token'] = unicode(user.user_id)

            self.write(response)

        except Exception, e:
            self.write_exception(e)
            self.finish()

class LogoutHandler(BaseHandler):
    def post(self):
        try:
            #if self.session:
            #    self.session.clear()
            #    self.clear_cookie('sid', "/", self.settings["cookie_domain"])

            response = dict()
            response.update(success={'code': 1})
            self.write(response)

        except Exception, e:
            self.write_exception(e)

