import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS , cross_origin
import random
import sys

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
  # create and configure the app  
  app = Flask(__name__)
  # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  setup_db(app)
  cors = CORS(app, resources={r"*": {"origins": "*"}})
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''

  # CORS Headers 
  @app.after_request
  def after_request(response):
    # response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response
    '''
    @TODO: 
    Create an endpoint to handle GET requests 
    for all available categories.
    '''

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

  @app.route('/api/questions', methods=['GET'])
  @cross_origin()
  def getQuestions():
    page = request.args.get('page', 1, type=int)
    # 2 elements for every page
    # start = (page - 1) * QUESTIONS_PER_PAGE
    # end = start + QUESTIONS_PER_PAGE

    try:
      questions =  Question.query.paginate(page, QUESTIONS_PER_PAGE, False) #Question.query.all()
      categories = Category.query.all()

      formated_category = [c.format() for c in categories]
      formated_questions = [q.format() for q in questions.items]


      total = questions.total

      return jsonify({
        'success':True,
        'questions':formated_questions,
        'total_questions':total,
        'categories':formated_category,
        'currentCategory':{}
        })
    
    except Exception as e:
        abort(422)
        # abort(422,"Unprocessable Entity : The error occurs when your data is incorrect; or for the lack of better terms, doesn't make logical sense.")
        print(e)

  @app.route('/api/categories', methods=['GET'])
  @cross_origin()
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

  @app.route('/api/questions/<int:question_id>', methods=['DELETE'])
  @cross_origin()
  def delete_question(question_id):
    # question = Question.query.get(id=question_id).one_or_none()

    # if(question is None):
    #     abort(404)

    try:
        question = Question.query.get(question_id)
        Question.delete(question)        
        return jsonify({
              'success':True,
        })
    except Exception as e:
        print(e)
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

  @app.route('/api/question', methods=['POST'])
  @cross_origin()
  def add_question():
    try:
      # formData = Question(request.get_json().get('question'),request.get_json().get('answer'),request.get_json().get('category'),request.get_json().get('difficulty'))
      formData = Question('', '', 0, 0)
      formData.question = request.get_json().get('question')
      formData.category = request.get_json().get('category')
      formData.answer = request.get_json().get('answer')
      formData.difficulty = request.get_json().get('difficulty')
      #print(formData.question)

      if(formData.question and formData.answer and formData.category and formData.difficulty):
        Question.insert(formData)
        return jsonify({
          'success':True
        })  
      else:
         return jsonify({
          'success':False,
          'message':'Check All required Fields'

        })
    except Exception as e:
      print(e)
      abort(422)

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  @app.route('/api/questions/search', methods=['POST'])
  @cross_origin()
  def search_questions():

    searchTerm = request.get_json().get('searchTerm')
    res = Question.query.filter(Question.question.ilike("%" + searchTerm + "%")).all()
  
    formated_questions = [q.format() for q in res]

    return jsonify({
      'success':True,
      'questions':formated_questions,
      'total_questions':len(res),
      'currentCategory':{}
      })

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

  @app.route('/api/categories/<int:id>/questions', methods=['GET'])
  @cross_origin()
  def getQuestionsOfCategory(id):
    question = Question('', '', 0, 0)
    questions = Question.getQuestionsAndCategories(question).filter(Category.id == id).all()
    currentCategory = Category.query.get(id)
    # print(questions)

    formated_questions = []
    for q in questions:
      formated_questions.append({
      'id': q[0],
      'question': q[1],
      'answer': q[2],
      'category': q[3],
      'difficulty': q[4]
    })

    # formated_questions = [q.format() for q in questions]
    # print(formated_questions)

    return jsonify({
      'success':True,
      'questions':formated_questions,
      'total_questions':len(formated_questions),
       'currentCategory':currentCategory.format()
      })

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

  @app.route('/api/quizzes', methods=['POST'])
  @cross_origin()
  def getQuiz():

    question = Question('', '', 0, 0)
    previousQuestions = request.get_json().get('previous_questions')
    quizCategory = request.get_json().get('quiz_category')
    print(quizCategory)

    if(quizCategory['id'] == 0):
       questions = Question.getQuestionsAndCategories(question).all()
    else:
       questions = Question.getQuestionsAndCategories(question).filter(Category.id == quizCategory['id']).all()
    
    formated_questions = []
    for q in questions:
      formated_questions.append({
      'id': q[0],
      'question': q[1],
      'answer': q[2],
      'category': q[3],
      'difficulty': q[4]
    })

    question = random.choice(formated_questions)

    canSendit = True

    print(previousQuestions)
    print(question)

    count = len(formated_questions)

    while count > 0:
      print(count)
      count -= 1

      if(question['id'] in previousQuestions):
          canSendit = False
          question = random.choice(formated_questions)
          print(question)
      else:
          canSendit = True
          break

      if(len(previousQuestions) == len(formated_questions)):
          canSendit = False
          break

    if(canSendit):
      return jsonify({
        'success':True,
        'question':question
        })
    else:
      return jsonify({
        'success':False,
        'question':'',
        'message':'You answered all questions'
        })

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
          "message": error.description
          }), 404

  @app.errorhandler(422)
  def unprocessable_entity(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message":"Unprocessable Entity : The error occurs when your data is incorrect; or for the lack of better terms, doesn't make logical sense."
           #error.description
          }), 422

  return app
    
