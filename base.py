from tornado import web

class BaseHandler(web.RequestHandler):

    @property
    def db(self):
        return self.application.db
