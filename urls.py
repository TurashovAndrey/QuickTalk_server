import tornado.web
from handlers.test_handler import TestHandler
from handlers.login_handler import SignUpHandler, LoginHandler, LogoutHandler, ProfileHandler
from handlers.advert_handler import AdvertHandler, AdvertCategoriesHandler, AdvertSubCategoriesHandler
from handlers.user_comments_handler import UserCommentsHandler
from handlers.request_handler import RequestHandler
import redis
from helpers.session import RedisSessionStore


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", TestHandler),
            (r"/leasing/signup", SignUpHandler),
            (r"/leasing/login", LoginHandler),
            (r"/leasing/logout", LogoutHandler),
            (r"/leasing/updateProfile", ProfileHandler),
            (r"/leasing/getAdvert", AdvertHandler),
            (r"/leasing/createAdvert", AdvertHandler),
            (r"/leasing/getCategories", AdvertCategoriesHandler),
            (r"/leasing/getSubCategories", AdvertSubCategoriesHandler),
            (r"/leasing/getUserComments", UserCommentsHandler),
            (r"/leasing/createUserComment", UserCommentsHandler),
            (r"/leasing/getRequests", RequestHandler),
            (r"/leasing/createRequest", RequestHandler)
        ]
        settings = dict(
            debug=True,
            login_url="/login",
            cookie_secret="yVJwZeaTRN+RNaFJ8cXVuacVBDsvSEZjqqg9tzaXTI0=",
            cookie_domain="fahlo.loc"
        )

        tornado.web.Application.__init__(self, handlers, **settings)
        self.redis = redis.StrictRedis()
        self.session_store = RedisSessionStore(self.redis)


if __name__ == "__main__":
    application = Application()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
