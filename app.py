from flask import Flask, request, abort, jsonify, render_template, redirect, url_for
from models import app, db, Actor, Movie
from flask_cors import CORS
import sys
from config import SQLALCHEMY_DATABASE_URI
# from auth import AuthError, requires_auth



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
def index():
    # return "Flask app"
    return  redirect(url_for("retrieve_actors"))


#  get all actors
@app.route("/actors", methods=["GET"])
# @requires_auth("get:actors&movies")
# def retrieve_actors(jwt):
def retrieve_actors():

    try:
        actors = Actor.query.all()

        return render_template("actors.html", data=Actor.query.all())
   

    except:
        abort(404)

#  get all movies
@app.route("/movies", methods=["GET"])
# @requires_auth("get:actors&movies")
# def retrieve_movies(jwt):
def retrieve_movies():

    try:
        movies = Movie.query.all()

        return render_template("movies.html", data=Movie.query.all())
  

    except:
        abort(404)


# get specific actor by id
@app.route("/actors/<int:actor_id>", methods=["GET"])
   
def get_specific_actor(actor_id):

    try:
        actor = db.session.query(Actor).filter(Actor.id == actor_id).all()

        return render_template("/show_actor.html", data=actor)

    except Exception as e:
        abort(404)

    finally:
        db.session.close()


# add actor
@app.route("/actors", methods=["POST"])
# @requires_auth("add&delete:actor")
def create_actor():
    try:
        attributes_name = request.form.get("attributes_name", "")
        age = request.form.get("age", "")
        gender = request.form.get("gender", "")
        actor = Actor(attributes_name=attributes_name, age=age, gender=gender)
        db.session.add(actor)
        db.session.commit()

        return render_template("/actors.html", data=Actor.query.all())

    except Exception as e:
        db.session.rollback()
        print(sys.exc_info())
        abort(405)

    finally:
        db.session.close()

# add movie
@app.route("/movies", methods=["POST"])
# @requires_auth("add&delete:movie")
def create_movie():
    try:
        attributes_title = request.form.get("attributes_title", "")
        release_date = request.form.get("release_date", "")
        actor_id = request.form.get("actor_id", "")
        movie = Movie(attributes_title=attributes_title, release_date=release_date, actor_id=actor_id)
        db.session.add(movie)
        db.session.commit()

        return render_template("/movies.html", data=Movie.query.all())

    except Exception as e:
        db.session.rollback()
        print(sys.exc_info())
        abort(405)

    finally:
        db.session.close()


    # delete actor 
@app.route("/delete/<int:id>")
# @requires_auth("add&delete:actor")  
# def delete_actor(jwt,id):
def delete_actor(id):
    actor = Actor.query.get_or_404(id)
    try:
        db.session.delete(actor)
        db.session.commit()

        return render_template("actors.html", data=Actor.query.all())

    except Exception as e:
        db.session.rollback()
        print(sys.exc_info())
        abort(422)

    finally:
        db.session.close()



# update actor
@app.route("/update/<int:id>", methods=['POST','GET'])
# @requires_auth("patch:actors&movies")
# def update(jwt,id):
def update(id):
    actor_to_update = Actor.query.get_or_404(id)
    if request.method == 'POST':
        actor_to_update.attributes_name = request.form["attributes_name"]
        try:
            db.session.commit()
            return render_template("actors.html", data=Actor.query.all())
        except Exception as e:
            db.session.rollback()
            print(sys.exc_info())
            abort(405)
        finally:
            db.session.close()
    else:
        return render_template("update_actor.html", actor_to_update=actor_to_update)





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
# @app.errorhandler(AuthError)
# def auth_error(e):
#     return jsonify(e.error), e.status_code

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