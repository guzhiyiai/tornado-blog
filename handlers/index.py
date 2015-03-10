# -*- coding: utf-8 -*-



from base import BaseHandler
from model.post import Post


class MainHandler(BaseHandler):
    def get(self):
        db = self.db()
        post = db.query(Post).filter_by().first()
        self.render('index.html', post=post)



class FormHandler(BaseHandler):
    def get(self):
        self.render("index.html", post="xxx")

    def post(self):
        uname = self.get_argument("uname", "")
        self.write(uname)
