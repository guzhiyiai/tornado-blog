# -*- coding: utf-8 -*-

from base import BaseHandler
from models.post import Post
import tornado.web

from service import PostService


class MainHandler(BaseHandler):
    def get(self):
        posts = PostService.get_list()

        self.render('index.html', posts=posts)


class HomeHandler(BaseHandler):
    # @tornado.web.authenticated
    def get(self):
        posts = PostService.get_list()
        self.render('index.html', posts=posts)

    def post(self):
        title = self.get_argument("title", None)
        content = self.get_argument("content", None)
        post = PostService.add(title, content)
        self.write(post)


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
