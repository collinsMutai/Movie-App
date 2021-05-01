import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            "postgres", "7749", "localhost:5432", self.database_name
        )

        setup_db(self.app, self.database_path)

        self.new_actor = {
            "attributes_name" : "James",
            "age" : "45",
            "gender" : "Male"
        }

        self.new_movie = {
            "attributes_title" : "Will Smitt",
            "release_date" : "2021-2-05",
            "actor_id" : "2"
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    
    """
# GET actors.
    def test_get_actors(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"],True)
        self.assertTrue(data["actors"])
        self.assertTrue(data["total_actors"])

    def test_get_actors_not_found(self):
        res = self.client().get("/actors/100")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

# GET movies.
    def test_get_movies(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"],True)
        self.assertTrue(data["movies"])
        self.assertTrue(data["total_movies"])

    def test_get_movies_not_found(self):
        res = self.client().get("/movies/100")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")


#  DELETE actor with id.

    def test_delete_actors(self):
        res = self.client().delete("/actors/1")
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 1)
        self.assertTrue(data["actors"])
        self.assertTrue(data["total_actors"])
        self.assertEqual(actor, None)

    def test_delete_actors_not_found(self):
        res = self.client().delete("/actors/100")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable")

#  DELETE movie with id.

    def test_delete_movies(self):
        res = self.client().delete("/movies/1")
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 1)
        self.assertTrue(data["movies"])
        self.assertTrue(data["total_movies"])
        self.assertEqual(movie, None)

    def test_delete_movies_not_found(self):
        res = self.client().delete("/movies/100")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable")

# PATCH actor.

    def test_update_attribute_name(self):
        res = self.client().patch('/actors/1', json={'attributes_name': "Kevin Hart"})
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['attributes_name'], "Kevin Hart")
        

    def test_400_for_failed_update(self):
        res = self.client().patch('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

# PATCH movie.

    def test_update_attribute_title(self):
        res = self.client().patch('/movies/1', json={'attributes_title': "Chris Rock"})
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie.format()['attributes_title'], "Chris Rock")
        

    def test_400_for_failed_update(self):
        res = self.client().patch('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

    # POST new actor.

    def test_post_actor(self):
        res = self.client().post("/actors", json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])

        self.assertTrue(data["actors"])
        self.assertTrue(data["total_actors"])

    def test_post_new_actor_405(self):
        res = self.client().post("/actors/100", json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Method Not Allowed")

    # POST new movie.

    def test_post_movie(self):
        res = self.client().post("/movies", json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])

        self.assertTrue(data["movies"])
        self.assertTrue(data["total_movies"])

    def test_post_new_movie_405(self):
        res = self.client().post("/movies/100", json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Method Not Allowed")








# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()