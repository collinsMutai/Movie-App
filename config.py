import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = "postgres://postgres:7749@localhost:5432/capstonedb"

SQLALCHEMY_TRACK_MODIFICATIONS = False