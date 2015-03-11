# -*- coding: utf-8 -*-

from handlers.index import MainHandler
from handlers.index import LoginHandler, LogoutHandler, HomeHandler

urls = [
    (r'/', MainHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/edit', HomeHandler),
]
