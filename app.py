from flask import Flask, request, abort, jsonify, render_template, redirect, url_for
from models import app, db, Actor
from flask_cors import CORS
import sys
from config import SQLALCHEMY_DATABASE_URI


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
def index():

    return render_template("index.html", data=Actor.query.all())


#  get all actors
@app.route("/actors", methods=["GET"])
def retrieve_actors():

    try:
        actors = Actor.query.all()

        return render_template("actors.html", data=Actor.query.all())
    # return redirect(url_for("index.html"))

    except:
        abort(404)


# get specific actor by id
@app.route("/actors/<int:actor_id>", methods=["GET"])
def get_specific_actor(actor_id):

    try:
        actor = db.session.query(Actor).filter(Actor.id == actor_id).all()

        return render_template("/show_actor.html", data=actor)

    except:
        abort(404)

    finally:
        db.session.close()


# add new actor
@app.route("/actors/create", methods=["POST"])
def create_actor():
    try:
        attributes_name = request.form.get("attributes_name", "")
        age = request.form.get("age", "")
        gender = request.form.get("gender", "")
        actor = Actor(attributes_name=attributes_name, age=age, gender=gender)
        db.session.add(actor)
        db.session.commit()

        return render_template("/actors.html", data=Actor.query.all())

    except:
        abort(405)

    finally:
        db.session.close()


# delete specific actor by id
@app.route("/actors/<int:actor_id>", methods=["DELETE"])
def delete_actor(actor_id):
    try:

        actor = Actor.query.get(actor_id)
        db.session.delete(actor)

        db.session.commit()

        return render_template("/actors.html", data=Actor.query.all())

    except:
        abort(422)

    finally:
        db.session.close()


# edit specific actor by id
@app.route("/actors/<int:actor_id>", methods=["PATCH"])
def edit_actor(actor_id):
    try:

        actor = Actor.query.get(actor_id)
        actor.attributes_name = "My new Name"

        db.session.commit()

        return render_template("/actors.html", data=Actor.query.all())

    except:
        abort(422)

    finally:
        db.session.close()


# movies


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

    return app


# # pip freeze > requirements.txt
# # FLASK_APP=app.py FLASK_DEBUG=true flask run
# # pg_ctl -D "C:/Program Files/PostgreSQL/13/data" start
