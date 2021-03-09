from flask import Flask, request, abort, jsonify
from models import setup_db, Actor
from flask_cors import CORS


# Pagination

ACTORS_PER_SHELF = 0


def paginate_actors(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * ACTORS_PER_SHELF
    end = start + ACTORS_PER_SHELF

    actors = [actor.format() for actor in selection]
    current_actors = actors[start:end]

    return current_actors


# App Config.


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    @app.route("/")
    def get_greeting():

        return jsonify({"Greeting": "Hello!"})

    @app.route("/actors", methods=["GET"])
    def retrieve_actors():
        try:
            selection = Actor.query.order_by(Actor.id).all()
            current_actors = paginate_actors(request, selection)

            if len(current_actors) == 0:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "actors": current_actors,
                    "total_actors": len(Actor.query.all()),
                }
            )
        except:
            abort(404)

    # @app.route("/actors/<int:actor_id>", methods=["GET"])
    # def get_specific_actor(actor_id):

    #     try:

    #         actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    #         current_actors = paginate_actors(request, selection)

    #         if len(current_actors) == 0:
    #             abort(404)

    #         return jsonify(
    #             {
    #                 "success": True,
    #                 "actors": current_actors,
    #                 "total_actors": len(current_actors),
    #             }
    #         )

    #     except:
    #         abort(404)

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
                    "error": 405,
                    "message": "The method is not allowed for the requested URL",
                }
            ),
            405,
        )

    return app

    # pip freeze > requirements.txt
    # FLASK_APP=app.py FLASK_DEBUG=true flask run
    # pg_ctl -D "C:/Program Files/PostgreSQL/13/data" start
