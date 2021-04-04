from flask import Flask, request, abort, jsonify, render_template, redirect, url_for
from models import db, setup_db, Actor
from flask_cors import CORS
from auth import AuthError, requires_auth
import sys

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
        response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        return response


    @app.route("/")
    def home():
        return redirect(url_for("actors"))


    #  get and post all actors
    @app.route("/actors", methods=['POST','GET'])
   
    def actors():
        if request.method == 'POST':
            attributes_name = request.form.get("attributes_name", "")
            age = request.form.get("age", "")
            gender = request.form.get("gender", "")
            actor = Actor(attributes_name=attributes_name, age=age, gender=gender)
            try:

                db.session.add(actor)
                db.session.commit()
                return render_template("actors.html", data=Actor.query.all())
            except Exception as e:
                db.session.rollback()
                print(sys.exc_info())
                abort(405)

            finally:
                db.session.close()
        else:
            return render_template("actors.html", data=Actor.query.all())
   
   
    # update actor
    @app.route("/update/<int:id>", methods=['POST','GET'])
  
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





    # delete specific actor by id
    @app.route("/delete/<int:id>")
    
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


    # # pip freeze > requirements.txt
    # # FLASK_APP=app.py FLASK_DEBUG=true flask run
    # # pg_ctl -D "C:/Program Files/PostgreSQL/13/data" start
