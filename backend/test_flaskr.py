import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

import json
import requests

from flaskr import create_app
from models import setup_db, Question, Category

#using https://stackoverflow.com/questions/32665659/typeerror-response-object-has-no-attribute-getitem

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    url = 'http://127.0.0.1:5000/api'
    newQuestion ={
        'question':'New Question',
        'answer':'New Answer',
        'difficulty':2,
        'category':1
    }

    quiz_request = {
        'previous_questions': [8],
         'quiz_category': {'type': "geography", 'id': 2}
    }
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia"
        self.driver_name ="postgres"
        self.user_name ="mohamed@localhost"
        #self.database_path = "postgres://{driver_name}/{user_name}".format('localhost:5432', self.database_name)
        self.database_path = 'postgresql://'+self.driver_name+':'+self.user_name+':5432/'+self.database_name

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_404_sent(self):
        response = requests.get(self.url +'/no_page')
        data = response.json()
        self.assertTrue(data['message'],'Not Found')
        self.assertEqual(data['success'],False)

     #Fauiler : Should be not found error , success:False
    def test_addQuestionWithError(self):
        response = requests.post(self.url +'/api/question',json = self.newQuestion)
        data = response.json()
        self.assertEqual(data['success'],False)


    def test_getQuestions(self):
        response = requests.get(self.url +'/questions')
        data = response.json()
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['success'],True)

    def test_getCategories(self):
        response = requests.get(self.url +'/categories')
        data = response.json()
        self.assertTrue(data['categories'])
        self.assertTrue(data['total_categories'])
        self.assertEqual(data['success'],True)

    
    def test_searchQuestion(self):
        response = requests.post(self.url +'/questions/search',json = {'searchTerm':'is'})
        data = response.json()
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['success'],True)
        
    def test_deleteQuestion(self):
        response = requests.delete(self.url +'/questions/19')
        
        data = response.json()
        self.assertEqual(data['success'],True)

    def test_getQuestionsByCategories(self):
        response = requests.get(self.url +'/categories/1/questions')
        
        data = response.json()
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['currentCategory'])
        self.assertEqual(data['success'],True)

    def test_addQuestion(self):
        response = requests.post(self.url +'/question',json = self.newQuestion)
        
        data = response.json()
        self.assertEqual(data['success'],True)

    def test_quizzes(self):
        response = requests.post(self.url +'/quizzes',json = self.quiz_request)
        
        data = response.json()
        self.assertTrue(data['question'])
        self.assertEqual(data['success'],True)

    




    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()