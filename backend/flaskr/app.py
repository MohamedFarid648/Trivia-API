import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS ,cross_origin
import random
import sys

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
  # create and configure the app  
  app = Flask(__name__, instance_relative_config=True)
  CORS(app)
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''


  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''


  # CORS Headers 
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response
    '''
    @TODO: 
    Create an endpoint to handle GET requests 
    for all available categories.
    '''


  @app.route("/api/hello")
  @cross_origin()
  def get_greeting():
      return jsonify({'message':'Hello, World!'})


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 
  

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''



  @app.route('/api/questions',methods=['GET'])
  def getQuestions():
    page = request.args.get('page', 1, type=int)
    #2 elements for every page
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = Question.query.all()
    categories = Category.query.all()

    formated_questions = [q.format() for q in questions]
    formated_category = [c.format() for c in categories]

    print(page)
    return jsonify({
      'success':True,
      'questions':formated_questions[start:end],
      'total_questions':len(questions),
      'categories':formated_category,
      #'currentCategory':
      })

  @app.route('/api/categories',methods=['GET'])
  def getCategories():
    categories = Category.query.all()
    formated_category = [c.format() for c in categories]
    
    return jsonify({
      'success':True,
      'total_categories':len(categories),
      'categories':formated_category,
      })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/api/question/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question = Question.query.filter_by(id=question_id).one_or_none()

    if(question is None):
        abort(404)

    try:
        Question.delete(question)
        return jsonify({
              'success':True,
        })
    except:
        abort(422)
 
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False, 
          "error": 404,
          "message": "Not found"
          }), 404

  @app.errorhandler(404)
  def unprocessable_entity(error):
      return jsonify({
          "success": False, 
          "error": 422,
          "message": "Unprocessable Entity"
          }), 422

  return app
    