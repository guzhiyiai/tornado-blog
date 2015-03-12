# -*- coding: utf-8 -*-

from models import Post
from extensions import db


class PostService(object):

    @staticmethod
    def add(title, content):
        post = Post(title=title, content=content)
        db.add(post)
        db.commit()
        return post.to_dict()

    @staticmethod
    def get_list():
        posts = Post.query.all()
        return [post.to_dict() for post in posts]
