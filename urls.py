import tornado.web
from handlers.users_handler import SignUpHandler, LoginHandler, LogoutHandler, ProfileHandler, UsersHandler, LiveUsersHandler
import redis
from helpers.session import RedisSessionStore
from handlers.request_handler import RequestHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/job/signup", SignUpHandler),
            (r"/job/login", LoginHandler),
            (r"/job/logout", LogoutHandler),
            (r"/job/profile", ProfileHandler),

            (r"/job/users", UsersHandler),

            (r"/job/liveUsers", LiveUsersHandler),

            (r"/job/liveGroups", UsersHandler),

            (r"/job/requests", RequestHandler),

            (r"/job/userComments", UsersHandler),
            (r"/job/userComments", UsersHandler),

            (r"/job/cities", UsersHandler),
        ]
        settings = dict(
            debug=True,
            login_url="/login",
            cookie_secret="yVJwZeaTRN+RNaFJ8cXVuacVBDsvSEZjqqg9tzaXTI0=",
            cookie_domain="quicktalk.loc"
        )

        tornado.web.Application.__init__(self, handlers, **settings)
        self.redis = redis.StrictRedis()
        self.session_store = RedisSessionStore(self.redis)


if __name__ == "__main__":
    application = Application()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
