import tornado.web

from model.post import Post

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        post = Post.get('LGL')
	self.render('index.html', post=post)
