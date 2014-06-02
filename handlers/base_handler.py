import tornado.web
from helpers.session import Session
from tornado.web import *
import functools

def is_authenticated(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            res = {'error': {
                'code': 403,
                'message': 'Bad auth token (check auth cookie)'}
            }
            self.set_status(res['error']['code'], res['error']['message'])
            self.write(res)
            return
        return method(self, *args, **kwargs)
    return wrapper

class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.session['user'] if self.session and 'user' in self.session else None

    @property
    def session(self):
        sessionid = self.get_secure_cookie('sid')
        return Session(self.application.session_store, sessionid)

    def write_exception(self, e, status_code=400, code=1):

        exc_type, exc_value, exc_traceback = sys.exc_info()

        if isinstance(e, HTTPError):
            status_code = e.status_code

        sys_msg = "" + type(e).__name__ + " was raised"
        msg = e.message
        self.set_status(status_code)

        res = {'error': {'code': code,
                         'sys_msg': sys_msg,
                         'message': msg, "traces": traceback.format_tb(exc_traceback)}}

        if hasattr(e, 'log_message'):
            res['error']['message'] += '\n' + e.log_message

        if hasattr(e, 'strerror'):
            print(e.strerror)

        self.write(res)
