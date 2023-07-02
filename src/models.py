import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class MyUser(Base):
    __tablename__ = 'my_user'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    favorite = relationship("Favorite")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('my_user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    alive = Column(Boolean, nullable=False)
    gender_id = Column(Integer, ForeignKey('gender.id'), nullable=False)
    favorite = relationship("Favorite")
    starship = relationship("Starship")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    favorite = relationship("Favorite")

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False, unique=True)
    model = Column(String(250), nullable=False, unique=True)
    max_speed = Column(Integer)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)

class Gender(Base):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True, nullable=False)
    gender_type = Column(String(250), nullable=False, unique=True)
    character = relationship("Gender")


render_er(Base, 'diagram.png')
