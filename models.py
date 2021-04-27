import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()





class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    attributes_name = db.Column(db.String())
    age = db.Column(db.String())
    gender = db.Column(db.String())
    actorsId = db.relationship(
        "Movie", backref="Actor", lazy=True, cascade="all, delete-orphan"
    )

  


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

    id = db.Column(db.Integer, primary_key=True)
    attributes_title = db.Column(db.String())
    release_date = db.Column(db.DateTime, default=datetime.utcnow)
    actor_id = db.Column(db.Integer, db.ForeignKey("actors.id"))


    def __init__(self, attributes_title, release_date, actor_id):
        self.attributes_title = attributes_title
        self.release_date = release_date
        self.actor_id = actor_id


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
            "actor_id": self.actor_id,
        }


