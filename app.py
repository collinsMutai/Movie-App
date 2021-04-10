from flask import Flask, request, abort, jsonify, render_template, redirect, url_for
from models import app, db, Actor, Movie
from flask_cors import CORS
import sys
from config import SQLALCHEMY_DATABASE_URI
from auth import AuthError, requires_auth



ACTORS_PER_PAGE = 10

def paginate_actors(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * ACTORS_PER_PAGE
    end = start + ACTORS_PER_PAGE

    actors = [actor.format() for actor in selection]
    current_actors = actors[start:end]

    return current_actors

# App Config.
app = Flask(__name__)

app.config.from_object("config")
db.init_app(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI


@app.after_request
def after_request(response):
    response.headers.add(
        "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response


@app.route("/")
# @requires_auth("get:actors&movies")
def index():


    return  "Flask App"


#  get all actors
@app.route("/actors", methods=["GET"])
def retrieve_actors():
    try:
        actors = Actor.query.order_by(Actor.id).all()
        current_actors = paginate_actors(request, actors)

        if len(current_actors) == 0:
            abort(404)

        return jsonify({
            "success": True,
            "actors": current_actors,
            "total_actors": len(Actor.query.all())
        })
    except:
        abort(404)







# error Handling
# 404
@app.errorhandler(404)
def not_found(error):
    return (
        jsonify({"success": False, "error": 404, "message": "Resource Not Found"}),
        404,
    )


# 405
@app.errorhandler(405)
def method_not_allowed(error):
    return (
        jsonify(
            {
                "success": False,
                "eror": 405,
                "message": "The method is not allowed for the requested URL",
            }
        ),
        405,
    )


# 422
@app.errorhandler(422)
def unprocessable(error):
    return (
        jsonify({"success": False, "error": 422, "message": "unprocessable"}),
        422,
    )


# 400
@app.errorhandler(400)
def bad_request(error):
    return (
        jsonify({"success": False, "error": 400, "message": "Bad Request"}),
        400,
    )


# 403
@app.errorhandler(403)
def forbidden(error):
    return (
        jsonify({"success": False, "error": 403, "message": "Forbidden"}),
        403,
    )


# 500
@app.errorhandler(500)
def internal_server_error(error):
    return (
        jsonify({"success": False, "error": 500, "message": "Internal Server Error"}),
        500,
    )


# error handler for AuthError
@app.errorhandler(AuthError)
def auth_error(e):
    return jsonify(e.error), e.status_code

    return app

# pip install -r requirements.txt
# # pip freeze > requirements.txt
# # FLASK_APP=app.py FLASK_DEBUG=true flask run
# # pg_ctl -D "C:/Program Files/PostgreSQL/13/data" start

# Casting Assistant 
# get:actors&movies	Can view actors and movies

# Casting Director 
# get:actors&movies	Can view actors and movies
# add&delete:actor	Add or delete an actor from the database
# patch:actors&movies	Modify actors or movies

# Executive Producer
# get:actors&movies	Can view actors and movies
# add&delete:actor	Add or delete an actor from the database
# patch:actors&movies	Modify actors or movies
# add&delete:movie	Add or delete a movie from the database