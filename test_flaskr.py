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

        self.new_question = {
            "attributes_name" : "James",
            "age" : "45",
            "gender" : "Male"
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
        self.assertEqual(data["success"],
        self.assertTrue(data["actors"]),True)
        self.assertTrue(data["total_actors"])

    def test_get_categories_not_found(self):
        res = self.client().get("/actors/100")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

    #  GET questions.
    # def test_paginated_questions(self):
    #     res = self.client().get("/questions")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(data["questions"])
    #     self.assertTrue(data["total_questions"])

    # def test_404_sent_requesting_beyond_valid_page(self):
    #     res = self.client().get("/questions?page=1000", json={"category": 1})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Resource Not Found")

    # # DELETE with question_id.

    # def test_delete_questions(self):
    #     res = self.client().delete("/questions/2")
    #     data = json.loads(res.data)

    #     question = Question.query.filter(Question.id == 1).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertEqual(data["deleted"], 2)
    #     self.assertTrue(data["questions"])
    #     self.assertTrue(data["total_questions"])
    #     self.assertEqual(question, None)

    # def test_delete_questions_not_found(self):
    #     res = self.client().delete("/questions/100")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Unprocessable")

    # # POST new question.

    # def test_post_new_question(self):
    #     res = self.client().post("/questions", json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(data["created"])

    #     self.assertTrue(data["questions"])
    #     self.assertTrue(data["total_questions"])

    # def test_post_new_question_405(self):
    #     res = self.client().post("/questions/100", json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Method Not Allowed")








# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()