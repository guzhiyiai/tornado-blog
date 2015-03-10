# -*- coding: utf-8 -*-

from handlers.index import MainHandler
from handlers.index import FormHandler

urls = [
    (r'/', MainHandler),
    (r'/form', FormHandler),
]
