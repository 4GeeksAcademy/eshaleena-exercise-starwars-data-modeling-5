import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250))
    dob = Column(DateTime)
    last_login_time = Column(DateTime)

class User(Base):
    __tablename__ = 'user'
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.user_id'))
   
class Media(Base):
    __tablename__ = 'media'
    follow_id = Column(Integer, primary_key=True)
    user_id1 = Column(Integer, ForeignKey('user.user_id'))
    user_id2 = Column(Integer, ForeignKey('user.user_id'))

class Post(Base):
    __tablename__ = 'post'
    feed_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    content = Column(String(250))
    photo_id = Column(Integer, ForeignKey('photo.photo_id'))
    creation_date = Column(DateTime, default=datetime.utcnow)
    photo = relationship(Photo)

    class Comment(Base):
    __tablename__ = 'comment'
    feed_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    content = Column(String(250))
    photo_id = Column(Integer, ForeignKey('photo.photo_id'))
    creation_date = Column(DateTime, default=datetime.utcnow)
    photo = relationship(Photo)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
