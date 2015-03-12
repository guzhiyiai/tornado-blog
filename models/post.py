# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text

from extensions import Base


# 定义对象:
class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column('title', String(50))
    content = Column('content', Text, default='', nullable=False)

    def to_dict(self):
        return dict(
                id = self.id,
                title = self.title,
                content = self.content
            )


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(50))
    email = Column('email', String(50), nullable=False, unique=True)

    def to_dict(self):
        return dict(
                id = self.id,
                name = self.name,
                email = self.email
            )
