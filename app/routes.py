import json
from app import app


@app.route('/temp/version/api/posts')
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
    return json.dump(posts)


@app.route('/temp/version/api/user/id')
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

    return json.dump(user)
