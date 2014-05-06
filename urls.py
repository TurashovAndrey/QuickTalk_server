import tornado.web
from handlers.test_handler import TestHandler

application = tornado.web.Application([
    (r"/", TestHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
