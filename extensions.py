# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.post import Base

# 初始化数据库连接(torndb):
# self.db = torndb.Connection("localhost", "tornado-test", user="root", password="abc123")

# 初始化数据库连接(sql):
engine = create_engine('mysql://root:abc123@localhost/tornado-test', echo=True)
# 创建DBSession类型:
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine, autocommit=True)
db = scoped_session(sessionmaker(bind=engine))
