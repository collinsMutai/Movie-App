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

- Base URL: At present this app can be run locally and also on heroku. The backend app is hosted at the default, http://127.0.0.1:5000/ or by visiting https://capstoneprojectdb.herokuapp.com/ , which set as a proxy in the frontend configuration.
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

  - Returns actors object, success value, and total number of actors

- Sample: curl -X GET http://127.0.0.1:5000/actors
  "actors": [
  {
  "age": "32",
  "attributes_name": "Samuel L Jackson",
  "gender": "Male",
  "id": 1
  },
  {
  "age": "",
  "attributes_name": "Dwayne Johnson",
  "gender": "Male",
  "id": 2
  },
  {
  "age": "",
  "attributes_name": "Jet Lee",
  "gender": "Male",
  "id": 3
  }
  ],
  "success": true,
  "total_actors": 3
  }

### GET/movies

- General:

- Sample: curl -X GET http://127.0.0.1:5000/movies
  "movies": [
  {
  "actor_id": 1,
  "attributes_title": "Wakanda",
  "id": 1,
  "release_date": "2021-27-04"
  },
  {
  "actor_id": null,
  "attributes_title": "Family Weekend",
  "id": 2,
  "release_date": "2021-27-04"
  },
  {
  "actor_id": 1,
  "attributes_title": "Death at a funeral",
  "id": 3,
  "release_date": "2021-27-04"
  }
  ],
  "success": true,
  "total_movies": 3
  }

### DELETE/actors/<int:id>

- General:

  - Deletes an actor based on id and returns actors object, id of deleted actor, success message and value

- Sample: curl -X DELETE http://127.0.0.1:5000/actors/4
  "actors": [
  {
  "age": "",
  "attributes_name": "Dwayne Johnson",
  "gender": "Male",
  "id": 2
  },
  {
  "age": "",
  "attributes_name": "Jet Lee",
  "gender": "Male",
  "id": 3
  }
  ],
  "deleted": 4,
  "success": true,
  "total_actors": 2
  }

### DELETE/movies/<int:id>

- General:

  - Deletes a movie based on id and returns actors object, id of deleted movie, success message and value

- Sample: curl -X DELETE http://127.0.0.1:5000/movies/3
  "deleted": 2,
  "movies": [
  {
  "actor_id": 1,
  "attributes_title": "Wakanda",
  "id": 1,
  "release_date": "2021-27-04"
  },
  {
  "actor_id": 1,
  "attributes_title": "Death at a funeral",
  "id": 3,
  "release_date": "2021-27-04"
  }
  ],
  "success": true,
  "total_movies": 2
  }

### POST/actors

- General:

  - Creates a new actor, returns actors object, the id of created actor, success message and total number of actors

- Sample: curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{"attributes_name":"Morgan Freeman", "age":"45", "gender":"Male"}'
  "actors": [
  {
  "age": "",
  "attributes_name": "Dwayne Johnson",
  "gender": "Male",
  "id": 2
  },
  {
  "age": "",
  "attributes_name": "Jet Lee",
  "gender": "Male",
  "id": 3
  },
  {
  "age": "45",
  "attributes_name": "Morgan Freeman",
  "gender": "Male",
  "id": 5
  }
  ],
  "created": 5,
  "success": true,
  "total_actors": 3
  }

### POST/movies

- General:

  - Creates a new movie, returns movie object, the id of created movie, success message and total number of movies

- Sample: curl http://127.0.0.1:5000/movies -X POST -H "Content-Type: application/json" -d '{"attributes_title":"Madea", "release_date":"2021-27-04", "actor_id":"1"}'
  "created": 4,
  "movies": [
  {
  "actor_id": 1,
  "attributes_title": "Wakanda",
  "id": 1,
  "release_date": "2021-27-04"
  },
  {
  "actor_id": 1,
  "attributes_title": "pirates of the caribbean",
  "id": 3,
  "release_date": "2021-27-04"
  },
  {
  "actor_id": 1,
  "attributes_title": "Madea",
  "id": 4,
  "release_date": "2021-27-04"
  }
  ],
  "success": true,
  "total_movies": 3
  }

### PATCH/actors

- General:

  - Updates the attributes_name of an actor, returns the id of updated actor, and a success message.

- Sample: curl http://127.0.0.1:5000/actors/2 -X PATCH -H "Content-Type: application/json" -d '{"attributes_name":"Collins"}'
  "success": true,
  "updated": 2
  }

### PATCH/movies

- General:

  - Updates the attributes_title of a movie, returns the id of updated movie, and a success message.

- Sample: curl http://127.0.0.1:5000/movies/3 -X PATCH -H "Content-Type: application/json" -d '{"attributes_title":"pirates of the caribbean"}'
  "success": true,
  "updated": 3
  }
