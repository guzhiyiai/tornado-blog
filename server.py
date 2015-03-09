import tornado.ioloop
import sys

from settings import application

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


