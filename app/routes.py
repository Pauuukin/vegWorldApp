import json
from app import app
#from datetime import datetime
#from flask_json import FlaskJSON, JsonError, json_response, as_json

@app.route('/')
@app.route('/index')
def index():
    str = "Hello, World!"
    return json.dumps(str)



# @app.route('/get_time')
# def get_time():
#     now = datetime.utcnow()
#     return json_response(time=now)
#


@app.route('/posts')
def posts():
    posts = [
        {
            'idPost': 123,
            'Author' : 'someUser',
            'Category': 'someCategory',
            'headline': 'someHeadline',
            'text': 'some text, some text, some text, some text, some text',
            'photo': 'когда-нибудь будет'
        },
        {
            'idPost': 124,
            'Author': 'another Some User',
            'Category': 'another Some Category',
            'headline': 'another Headline',
            'text': 'another some text,another some text, some text',
            'photo': 'когда-нибудь будет'
        },
        {
            'idPost': 128,
            'Author': 'another Some User 2',
            'Category': 'another Some Category 2',
            'headline': 'another Headline 2',
            'text': 'another some text 2 , another some text, some text 2 ',
            'photo': 'когда-нибудь будет'
        }
    ]
    return json.dumps(posts)


@app.route('/user/id')
def user():
    user = {
        'idUser' : 128,
        'fullName': 'Паукин Олег',
        'email' : 'oleg.paukin@mail.ru',
        'nickname': 'pauuukin',
        'phoneNumber': '89817802445',
        'gender': 'man',
        'aboutMe': 'some text; some text; some text; some text; some text; some text; ',
    }

    return json.dumps(user)
