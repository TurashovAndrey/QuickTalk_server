import tornado.web
from handlers.login_handler import SignUpHandler, LoginHandler, LogoutHandler, ProfileHandler
from handlers.cv_handler import CVHandler, AdvertCategoriesHandler, AdvertTypesHandler, AdvertsHandler
from handlers.cv_comments_handler import CVCommentsHandler
from handlers.cities_handler import CitiesHandler
from handlers.request_handler import RequestHandler
import redis
from helpers.session import RedisSessionStore


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/job/signup", SignUpHandler),
            (r"/job/login", LoginHandler),
            (r"/job/logout", LogoutHandler),
            (r"/job/profile", ProfileHandler),
            (r"/job/users", LoginHandler),
            (r"/job/getLiveUsers", AdvertsHandler),
            (r"/job/getLiveGroups", AdvertsHandler),
            (r"/job/getUserProfile", CVHandler),
            (r"/job/getRequests", RequestHandler),
            (r"/job/createRequest", RequestHandler),
            (r"/job/getUserComments", CVCommentsHandler),
            (r"/job/createUserComment", CVCommentsHandler),
            (r"/job/getCities", CitiesHandler),
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
