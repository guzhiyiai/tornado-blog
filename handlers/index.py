# -*- coding: utf-8 -*-

from base import BaseHandler
from model.post import Post
import tornado.web


class MainHandler(BaseHandler):
    def get(self):
        db = self.db()
        post = db.query(Post).filter_by().first()
        self.render('index.html', post=post)


class HomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        posts = self.db.query("SELECT * FROM post ORDER BY id" "DESC LIMIT 5")
        self.render('index.html', posts=posts)


class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        self.set_secure_cookie("username", self.get_argument("username"))
        self.redirect("/")


class LogoutHandler(BaseHandler):
    def get(self):
        if (self.get_argument("logout", None)):
            self.clear_cookie("username")
            self.redirect("/")
