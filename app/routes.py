import datetime
import json
from app import app, db
from flask_login import current_user, login_user, login_required
from app.models import User
from flask_login import logout_user
from datetime import datetime



def to_json(data):
    return json.dumps(data, ensure_ascii=False) + "\n"





@app.before_request
def before_request():
    """last seen realisation"""
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()




@app.route('/')
@app.route('/index')
def index():
    str = "привет мир!"
    return to_json(str)



# @app.route('/get_time')
# def get_time():
#     now = datetime.utcnow()
#     return json_response(time=now)
#



@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return "reg"
    user = 'def - some data'
    if user is None or not user.check_password(user.password):
        return 'no reg'
    return 'user api'




@app.route('/logout')
def logout():
    logout_user()
    return "some info"



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
    return to_json(posts)



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

    return to_json(user)


@app.route('/register', methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return "reg already complete"
    data = json.loads(user())
    return to_json(data)


@app.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_profile():
    data = json.loads(user())
    current_user.nickname = data['nickname']
    current_user.about_me = data['about_me']
    db.session.commit()
    return "changes have been saved"