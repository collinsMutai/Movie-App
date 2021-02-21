# import os
# from flask import Flask, request, abort, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# def create_app(test_config=None):
#   # create and configure the app
#   app = Flask(__name__)
#   CORS(app)

#   return app

# APP = create_app()

# if __name__ == '__main__':
#     APP.run(host='0.0.0.0', port=8080, debug=True)


import os
from flask import Flask, jsonify

# from models import setup_db


def create_app(test_config=None):

    app = Flask(__name__)
    # setup_db(app)
    # CORS(app)

    @app.route("/")
    def get_greeting():
        # excited = os.environ['EXCITED']
        # greeting = "Hello"
        # if excited == 'true': greeting = greeting + "!!!!!"
        # return greeting
        return jsonify({"Greeting": "Hello!"})

    # @app.route("/coolkids")
    # def be_cool():
    #     return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app


app = create_app()

if __name__ == "__main__":
    app.run()

    # FLASK_APP=app.py FLASK_DEBUG=true flask run