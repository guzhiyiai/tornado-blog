# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义对象:
class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column('title', String(50))
    content = Column('content', Text, default='', nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(50))
    email = Column('email', String(50), nullable=False, unique=True)
