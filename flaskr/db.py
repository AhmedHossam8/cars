import os
from sqlalchemy import create_engine, Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

db_string = os.getenv('CONNECTION_STRING')
db = create_engine("postgresql://postgres:1234@localhost:5432/cars_db")

base = declarative_base()
session = scoped_session(sessionmaker(db))


class user(base):
    __tablename__ = 'user'

    id = Column(String(128), unique=True, nullable=False, primary_key=True)
    username = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


class brand(base):
    __tablename__ = 'brand'
    id = Column(String(128), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)
    picture_url = Column(String, nullable=False)

    def __init__(self, id, name, picture_url):
        self.id = id
        self.name = name
        self.picture_url = picture_url


class Car(base):
    __tablename__ = 'car'
    id = Column(String(128), unique=True, nullable=False, primary_key=True)
    reference_id = Column(String(128), unique=True, nullable=False)
    name = Column(String(128), unique=True, nullable=False)
    brand_id = Column(String(128), ForeignKey('brand.id'), nullable=False)
    price = Column(Integer)

    def __init__(self, id, name, brand_id, price):
        self.id = id
        self.name = name
        self.brand_id = brand_id
        self.price = price


def init_db():
    base.metadata.create_all(db)