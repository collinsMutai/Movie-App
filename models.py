from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app, db)



class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    attributes_name = db.Column(db.String())
    age = db.Column(db.String())
    gender = db.Column(db.String())
    actorsId = db.relationship(
        "Movie", backref="Actor", lazy=True, cascade="all, delete-orphan"
    )

    # INSERT INTO actors (attributes_name, age, gender) VALUES ('Bond', '32', 'Male');


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
    release_date = db.Column(db.String())
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