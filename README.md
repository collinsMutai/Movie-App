# Capstone project

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./starter` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Introdution

- The capstone project follows RESTful principles, including naming of endpoints, use of HTTP methods GET , POST, PATCH and DELETE. The project handles errors using unittest library to test each endpoint for expected behaviour and error handling if applicable.

## Getting Started

- Base URL: At present this app can be run locally and also on heroku. The backend app is hosted at the default, http://127.0.0.1:5000/ or by visiting <--heroku-link -->, whixh set as a proxy in the frontend configuration.
- Authentication: This version of the application soes not require authentication or API keys.

## Error Handling

- Errors are returned as JSON objects in the following format:
  {
  "success": False,
  "error": 404,
  "message:" "Resource Not Found"
  }

The API will return four error types when requests fail:

- 404: Resource Not Found
- 422: Unprocessable
- 400: Bad Request
- 405: Method Not Allowed
- 403: Forbidden
- 500: Internal Server Error

## Endpoints

### GET/actors

- General:

- Sample: curl -X GET http://127.0.0.1:5000/actors

### GET/movies

- General:

- Sample: curl -X GET http://127.0.0.1:5000/movies

### DELETE/actors/<int:actor_id>

- General:

- Sample: curl -X DELETE http://127.0.0.1:5000/actors/10

### POST/actors

- General:

* Sample: curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{"attributes_name":"Samuel L. Jackson", "age":"45", "gender":"Male"}'

### GET/actors/<int:actor_id

- General:

* Sample: curl -X GET http://127.0.0.1:5000/questions/4
