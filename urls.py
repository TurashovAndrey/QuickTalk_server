import tornado.web
from handlers.test_handler import TestHandler
from handlers.login_handler import SignUpHandler, LoginHandler

application = tornado.web.Application([
    (r"/", TestHandler),
    (r"/signup", SignUpHandler),
    (r"/login", LoginHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
