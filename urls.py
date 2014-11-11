import tornado.web
from handlers.test_handler import TestHandler
from handlers.login_handler import SignUpHandler, LoginHandler, LogoutHandler, ProfileHandler
from handlers.advert_handler import AdvertHandler, AdvertCategoriesHandler, AdvertTypesHandler, AdvertsHandler
from handlers.advert_comments_handler import AdvertCommentsHandler
from handlers.cities_handler import CitiesHandler
from handlers.user_comments_handler import UserCommentsHandler
from handlers.request_handler import RequestHandler
import redis
from helpers.session import RedisSessionStore


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", TestHandler),
            (r"/job/signup", SignUpHandler),
            (r"/job/login", LoginHandler),
            (r"/job/logout", LogoutHandler),
            (r"/job/getProfile", ProfileHandler),
            (r"/job/updateProfile", ProfileHandler),
            (r"/job/getAdverts", AdvertsHandler),
            (r"/job/getAdvert", AdvertHandler),
            (r"/job/createAdvert", AdvertHandler),
            (r"/job/getCategories", AdvertCategoriesHandler),
            (r"/job/getTypes", AdvertTypesHandler),
            (r"/job/getUserComments", UserCommentsHandler),
            (r"/job/createUserComment", UserCommentsHandler),
            (r"/job/getRequests", RequestHandler),
            (r"/job/createRequest", RequestHandler),
            (r"/job/getAdvertComments", AdvertCommentsHandler),
            (r"/job/createAdvertComment", AdvertCommentsHandler),
            (r"/job/getCities", CitiesHandler)
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
