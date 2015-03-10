import os


template_path=os.path.join(os.path.dirname(__file__), "templates")
static_path=os.path.join(os.path.dirname(__file__), "static")

# 防跨站伪造请求
xsrf_cookies=True
cookie_secret="test-2001"






