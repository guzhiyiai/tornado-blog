import os

import tornado.web

from urls import urls

settings = dict(
template_path=os.path.join(os.path.dirname(__file__), "templates"),
static_path=os.path.join(os.path.dirname(__file__), "static"),
)

application = tornado.web.Application(handlers=urls, **settings)
