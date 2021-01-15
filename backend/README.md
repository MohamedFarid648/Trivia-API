# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 
```

Project Documentation : 

•	Project Title:
        Travia api
        It is a simple project to display categories and questions for each one and play a game for answer the questions .


•	Getting Started:
          install node , pip3 , paython
          in frontend folder run:
                                    npm install --save && npm start
          in backend folder run :
                                    pip install -r requirements.txt
                                    set FLASK_APP=flaskr
                                    set FLASK_ENV=development
                                    flask run

•	API Reference (Endpoints):

    1.GET '/api/categories'
    - Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
    - Request Arguments: None
    - Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs. 
    {'1' : "Science",
    '2' : "Art",
    '3' : "Geography",
    '4' : "History",
    '5' : "Entertainment",
    '6' : "Sports"}

    2.GET '/api/questions'
    - Return all questions with pagination
    - Request Arguments: pageNumber( 1 is default)
    - Returns: All Questions with pagination and All Categories. 
    questions:[
    {answer: "Maya Angelou", category: 1, difficulty: 4, id: 1, question: "Whose autobiography is entitled I Know Why the Caged Bird Sings?"},
    {answer: "Muhammad Ali", category: 1, difficulty: 4, id: 2, question: "What boxer s original name is Cassius Clay?"},
    {answer: "Apollo 13", category: 1, difficulty: 5, id: 3, question: "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"},
    {answer: "Tom Cruise", category: 1, difficulty: 6, id: 4, question: "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"},
    {answer: "ww", category: 1, difficulty: 1, id: 16, question: "rr"}]
    success: true,
    total_questions: 5}

    3.DELETE '/api/question/<int:id>'
    -  Delete Question depends on its id
    - Request Arguments:Question Id
    - Return {'success' :True} if the question is deleted

    4.POST '/api/question'
    -  Add New Question
    - Request Arguments:Question Object(question,answer,category,difficulty)
    - Return {'success' :True} if the question is inserted 
    and {'success' :False } if one of the values is empty

    5.POST '/api/questions/search'
    -  Search for  a question(s) using  string value
    - Request Arguments:Question Value as string
    - Return the questions that have a specific value
    Ex:If we search for a Whose value it will Return : 
    {     'success':True,
        'questions':
            [{answer: "Maya Angelou"
            category: 1
            difficulty: 4
            id: 1
            question: "Whose autobiography is entitled I Know Why the Caged Bird Sings?"
            }],
        'total_questions':1,
        'currentCategory':{}
    }


    6.GET '/api/categories/<int:id>/questions'
    - Return all questions for a specific category
    - Request Arguments: Category ID
    - Returns: All Questions For this Category. 
    {
    currentCategory:{id: 1 , type: "science"}
    questions:[
    {answer: "Maya Angelou", category: 1, difficulty: 4, id: 1, question: "Whose autobiography is entitled I Know Why the Caged Bird Sings?"},
    {answer: "Muhammad Ali", category: 1, difficulty: 4, id: 2, question: "What boxer s original name is Cassius Clay?"},
    {answer: "Apollo 13", category: 1, difficulty: 5, id: 3, question: "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"},
    {answer: "Tom Cruise", category: 1, difficulty: 6, id: 4, question: "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"},
    {answer: "ww", category: 1, difficulty: 1, id: 16, question: "rr"}]
    success: true,
    total_questions: 5}


    7.POST '/api/quizzes'
    -  Get a random question for a specific category but not in perviues questions
    - Request Arguments: 
            PreviousQuestions: The Questions that user answered before
            quizCategory : Current Category or All(id=0)

    - Return the question that should be answered or {'success':False} if all questions have been answered

    Ex:If we choose science category : for a Whose value it will Return : 
    { 
            answer: "Apollo 13"
            category: 1
            difficulty: 5
            id: 3
            question: "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            success: true
    }


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```