import os
from sqlalchemy import Column, String, Integer, create_engine , Sequence
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_name = "trivia"
#database_path = "postgres://{}/{}".format('localhost:5432', database_name)
database_path = 'postgresql://postgres:mohamed@localhost:5432/trivia'

db = SQLAlchemy()
 

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # db = SQLAlchemy(app, 'session_options={"expire_on_commit":false}')

    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

    db.create_all()

'''
Question

'''
class Question(db.Model):  
  __tablename__ = 'questions'

  id = Column(Integer,primary_key=True) #Sequence('user_id_seq')
  question = Column(String)
  answer = Column(String)
  #category = Column(Integer,db.ForeignKey('category.id'))
  category = Column(Integer)
  difficulty = Column(Integer)
  

  def __init__(self, question, answer, category, difficulty):
    self.question = question
    self.answer = answer
    self.category = category
    self.difficulty = difficulty

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def getQuestionsAndCategories(self):
    data =  db.session.query(Question.id,Question.question,Question.answer,Question.category,Question.difficulty,Category.type).join(Category,Question.category == Category.id)

    return data

  def format(self):
    return {
      'id': self.id,
      'question': self.question,
      'answer': self.answer,
      'category': self.category,
      'difficulty': self.difficulty
    }

'''
Category

'''
class Category(db.Model):  
  __tablename__ = 'categories'

  id = Column(Integer, primary_key=True)
  type = Column(String)
  #questions = db.relationship('Question',backref='myCategory')

  def __init__(self, type):
    self.type = type

  def format(self):
    return {
      'id': self.id,
      'type': self.type
    }