# -*- coding: utf-8 -*-

import sys
import os

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options
import torndb

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from urls import urls

import sys
sys.path.append("/Users/sniper/learn-code/tornado-web/blog")

define("port", default=8888, help="PORT", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        #路由设置
        handlers = urls

        #配置信息
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            # 防跨站伪造请求
            xsrf_cookies=False,
            cookie_secret="test-2001",
            login_url="/login",
            debug=True,                  #调试模式
        )
        #服务器初始化
        tornado.web.Application.__init__(self, handlers=urls, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


