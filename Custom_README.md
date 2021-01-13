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

•	API Reference :

 1.'/api/questions', methods=['GET']  return all questions with pagination
 2.'/api/categories', methods=['GET']  return all categories
 3.'/api/question/<int:id>', methods=['DELETE']   delete questions
 4.'/api/question', methods=['POST'] add new question
 5.'/api/questions/search', methods=['POST'] search for a question
 6.'/api/categories/<int:id>/questions', methods=['GET'] Get questions for category
 7.'/api/quizzes', methods=['POST']  Get random question for quiz