import os, sys
from flask import Flask, request, abort, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import setup_db, Actor, Movie


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
def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)



    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        return response


    @app.route("/")
    def index():


        return  "Flask App"


    #  get all actors

    @app.route("/actors", methods=["GET"])
    # @requires_auth("get:actors&movies")
    def retrieve_actors():
            
        actors = Actor.query.order_by(Actor.id).all()
        current_actors = paginate_actors(request, actors)

            
        if len(current_actors) == 0:
            abort(404)
                    
                
        total_actors = len(Actor.query.all())

        return jsonify({
            "success": True,
            "actors": current_actors,
            "total_actors": total_actors
            })



    #  Delete actor

    @app.route("/actors/<int:id>", methods=["DELETE"])
    @requires_auth("delete:actor")
    def delete_actor(jwt, id):
       
        try:

            actor = Actor.query.get(id)

            if actor is None:
                abort(404)

            actor.delete()

            actors = Actor.query.order_by(Actor.id).all()
            current_actors = paginate_actors(request, actors)

            total_actors = len(Actor.query.all())

            return jsonify(
                {
                    "success": True,
                    "deleted": actor.id,
                    "actors": current_actors,
                    "total_actors": total_actors
                }
            )

        except:
            abort(422)




    # Update actor
    @app.route("/actors/<int:actors_id>", methods=["PATCH"])
    @requires_auth("patch:actors&movies")
    def update_actor(token, actors_id):

        body = request.get_json()

        try:
            actor = Actor.query.filter(Actor.id == actors_id).one_or_none()
            if actor is None:
                abort(404)

            if "attributes_name" in body:
                actor.attributes_name= body.get("attributes_name")

                actor.update()

            return jsonify({
                "success": True, 
                "updated": actor.id,
                })
        except:

            abort(400)



    # Add new actor
    @app.route('/actors', methods=['POST'])
    @requires_auth("add:actor")
    def create_actor(payload):
        body = request.get_json()

        attributes_name = body.get('attributes_name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        

        try:
            actor = Actor(attributes_name=attributes_name, age=age, gender=gender)
            actor.insert()

            selection = Actor.query.order_by(Actor.id).all()
            current_actors = paginate_actors(request, selection)

            total_actors = len(Actor.query.all())

            return jsonify({
                'success': True,
                'created': actor.id,
                'actors': current_actors,
                'total_actors': total_actors
            })

        except:
            abort(422)


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
                        "message": "Method Not Allowed",
                }
            ),
            405,
        )


        # 422
    @app.errorhandler(422)
    def unprocessable(error):
        return (
                jsonify({"success": False, "error": 422, "message": "Unprocessable"}),
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

# INSERT INTO actors (attributes_name, age, gender) VALUES ('Bond', '32', 'Male');
# heroku pg:psql HEROKU_POSTGRESQL_RED_URL
# heroku pg:push capstonedb HEROKU_POSTGRESQL_RED_URL --app guarded-fjord-08535
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade

# heroku config --app  capstoneprojectdb
# heroku run python manage.py db upgrade --app   capstoneprojectdb  

# $ PGUSER=postgres PGPASSWORD=7749 heroku pg:push capstonedb DATABASE_URL --app  capstoneprojectdb 
# heroku pg:push capstonedb HEROKU_POSTGRESQL_RED_URL --app  capstoneprojectdb
# $ PGUSER=postgres PGPASSWORD=7749 heroku pg:pull DATABASE_URL capstonedb --app capstoneprojectdb

# export DATABASE_URL="postgres://postgres:7749@localhost:5432/capstonedb"