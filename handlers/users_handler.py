from base_handler import BaseHandler
from helpers.helper_functions import *
from models.user_model import UserModel
import uuid
import arrow
import bcrypt
from helpers.session import Session


class SignUpHandler(BaseHandler):
    def post(self):
        try:
            user = dict()

            username = get_json_argument(self.request.body, 'username', None)
            email = get_json_argument(self.request.body, 'email', None)
            password = get_json_argument(self.request.body,'password', None)

            if not email or not password or not username:
                raise Exception('Need username, email, password to create user.')

            if len(password) < 8:
                raise Exception('Password must be greater than 8 symbols')

            u = UserModel().get_user(email=email)
            if isinstance(u, UserModel) and u.user_id:
                raise Exception('User with email %s already exists' % email)

            u = UserModel().get_user(username=username)
            if isinstance(u, UserModel) and u.user_id:
                raise Exception('User with username %s already exists' % username)

            user_id = uuid.uuid4()
            created = arrow.utcnow().timestamp

            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(11))
            hashed = unicode(hashed)

            user['user_id'] = user_id
            user['username'] = username
            user['hashed_pw'] = hashed
            user['email'] = email
            user['created'] = created
            user['updated'] = created

            UserModel().create_user(**user)

            sid = self.session.sessionid
            session = Session(self.application.session_store, sid)
            session['username'] = user['username']
            session['user_id'] = user['user_id']
            response = dict()
            self.set_secure_cookie('sid', sid, expires_days=30, domain="quicktalk.loc")
            response['token'] = unicode(user['user_id'])
            response['username'] = unicode(user['username'])

            self.write(response)
        except Exception, e:
            self.write_exception(e)

class LoginHandler(BaseHandler):
    def post(self):
        try:
            response = dict()
            email = get_json_argument(self.request.body, "email", None)
            password = get_json_argument(self.request.body, "password", None)

            if email is None or password is None:
                raise Exception(u"You must supply a username and password.")

            user = UserModel().check_password(email, password)
            if user is None:
                raise Exception(u"Invalid username or password!")

            sid = self.session.sessionid
            session = Session(self.application.session_store, sid)
            session['username'] = user.username
            session['user_id'] = user.user_id
            session['first_name'] = user.first_name
            session['last_name'] = user.last_name
            self.set_secure_cookie('sid', sid, expires_days=30, domain="fahlo.loc")
            response['token'] = unicode(user.user_id)
            response['username'] = unicode(user.email)
            self.write(response)

        except Exception, e:
            self.write_exception(e)
            self.finish()

class LogoutHandler(BaseHandler):
    def post(self):
        try:
            if self.session:
                self.session.clear()
                self.clear_cookie('sid', "/", self.settings["cookie_domain"])

            response = dict()
            response.update(success={'code': 1})
            self.write(response)

        except Exception, e:
            self.write_exception(e)

class ProfileHandler(BaseHandler):
    def get(self):
        try:
            user = UserModel().get_user(user_id=self.session['user_id'])
            response = dict()
            response['user_id'] = str(user.user_id)
            response['username'] = user.username
            response['first_name'] = user.first_name
            response['last_name'] = user.last_name
            response['email'] = user.email
            response['telephone'] = user.telephone

            self.write(response)
        except Exception, e:
            self.write_exception(e)

    def post(self):
        try:
            response = dict()

            kw = dict()
            kw['user_id'] = self.session['user_id']
            kw['username'] = get_json_argument(self.request.body, "username", None)
            kw['first_name'] = get_json_argument(self.request.body, "first_name", None)
            kw['last_name'] = get_json_argument(self.request.body, "last_name", None)
            kw['email'] = get_json_argument(self.request.body, "email", None)
            kw['telephone'] = get_json_argument(self.request.body, "telephone", None)

            UserModel().update_user(**kw)

            response.update(success={'code': 1})
            self.write(response)

        except Exception, e:
            self.write_exception(e)

class UsersHandler(BaseHandler):
    def get(self):
        users = UserModel().get_users()

        response = []
        for user in users:
            user_dict = dict()
            user_dict['user_id'] = str(user.user_id)
            user_dict['user_name'] = user.user_name

            response.append(user_dict)

        self.write({"users": response})
