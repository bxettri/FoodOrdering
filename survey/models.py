# Create your models here.
from mongoengine import *
from datetime import datetime
import json

connect(db='db_survey')


class User(Document):
    full_name = StringField(max_length=200, required=True)
    dob = DateField()
    gender = StringField(max_length=20, required=True)
    email = EmailField(max_length=100, required=True, unique=True)
    username = StringField(required=True, max_length=25)
    password = StringField(required=True)
    profile_image = StringField()
    date_registered = DateTimeField(default=datetime.utcnow)

    def json(self):
        user_dict = {
            "full_name": self.full_name,
            "gender": self.gender,
            "dob": self.dob,
            "email": self.email,
            "username": self.username,
            "profile_image": self.profile_image
        }
        return json.dumps(user_dict)

    meta = {
        'indexes': [
            'email', 'full_name', 'gender', 'dob'
        ]
    }


class Questions(EmbeddedDocument):
    questions = StringField()
    options = ListField(StringField())

    def json(self):
        question_dict = {
            "questions": self.questions,
            "options": self.options
        }
        return json.dumps(question_dict)


class Survey(Document):
    title = StringField(max_length=200, required=True)
    description = StringField()
    start_date = DateTimeField(required=True)
    end_date = DateTimeField(required=True)
    user = ReferenceField(User)
    questions = ListField(EmbeddedDocumentField(Questions))

    # options = ListField(EmbeddedDocumentField(Questions.options))

    def json(self):
        survey_dict = {
            "title": self.title,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "questions": self.questions
        }
        return json.dumps(survey_dict)


# class Respondents(EmbeddedDocument):
#     email = StringField(required=True, max_length=50)
#     attendant_datetime = DateTimeField(default=datetime.utcnow)
#
#     def json(self):
#         respondents_dict = {
#             "email" : self.email,
#             "attendant_datetime" : self.attendant_datetime
#         }
#         return json.dumps(respondents_dict)

class Response(Document):
    repondent_email = StringField(required=True, max_length=50)
    respond_datetime = DateTimeField(default=datetime.utcnow)
    question = ReferenceField(Survey)

    def json(self):
        response_dict = {
            "respondent_email": self.repondent_email,
            "respond_datetime": self.respond_datetime,
            "question": self.question,
            "answer": self.answer
        }
        return json.dumps(response_dict)

    meta = {'allow_inheritance': True}


class singleResponse(Response):
    answer = StringField()


class multipleResponse(Response):
    answer = ListField()


print('Done DB')
#
# User = User(
#     full_name="Amit Pradhan",
#     gender = "Male",
#     # dob = "09/09/1997",
#     email = "amit.pradhan195adsdasd@gmail.com",
#     password = "abc123"
#     )
#
# User.save()
