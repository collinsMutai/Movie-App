import os
from flask import Flask
from sqlalchemy import Column, String, Integer, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


database_name = "capstonedb"
database_path = "postgresql://{}:{}@{}/{}".format(
    "postgres", "7749", "localhost:5432", database_name
)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()


class Actor(db.Model):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    attributes_name = Column(String())
    age = Column(String())
    gender = Column(String())


def __init__(self, attributes_name, age, gender):
    self.attributes_name = attributes_name
    self.age = age
    self.gender = gender


def insert(self):
    db.session.add(self)
    db.session.commit()


def update(self):
    db.session.commit()


def delete(self):
    db.session.delete(self)
    db.session.commit()


def format(self):
    return {
        "id": self.id,
        "attributes_name": self.attributes_name,
        "age": self.age,
        "gender": self.gender,
    }


# movies


class Movie(db.Model):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    attributes_title = Column(String())
    release_date = Column(String())


def __init__(self, attributes_title, release_date):
    self.attributes_title = attributes_title
    self.release_date = release_date


def insert(self):
    db.session.add(self)
    db.session.commit()


def update(self):
    db.session.commit()


def delete(self):
    db.session.delete(self)
    db.session.commit()


def format(self):
    return {
        "id": self.id,
        "attributes_title": self.attributes_title,
        "release_date": self.release_date,
    }
