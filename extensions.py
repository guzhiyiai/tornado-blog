# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


# 初始化数据库连接(sql):
engine = create_engine('mysql://root:abc123@localhost/tornado-test', echo=True)

# 创建db_session类型:
db = scoped_session(sessionmaker(bind=engine, autocommit=False))

# 创建对象的基类
Base = declarative_base()
Base.query = db.query_property()

def init_db():
    import blog.models
    Base.metadata.create_all(engine)
