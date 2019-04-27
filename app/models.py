from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    nickname = db.Column(db.String(32), unique = True)
    phoneNumber = db.Column(db.String(32), unique = True)
    password_hash = db.Column(db.String(128))
    gender = db.Column(db.String(32))
    aboutMe = db.Column(db.Text(600))
    dateOfBirth = db.Column(db.Date)
    dateOfReg = db.Column(db.DateTime, index = True, default = datetime.utcnow)


    def __repr__(self):
        """Сообщает, как печатать объект класса"""
        return '<User {}>'.format(self.nickname)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    parent_id = db.Column(db.Integer)


    def __repr__(self):
        """Сообщает, как печатать объект класса"""
        return 'Category {}'.format(self.name)

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    text = db.Column(db.Text(500))

    def __repr__(self):
        """Сообщает, как печатать объект класса"""
        return 'Status {}'.format(self.title)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    headline = db.Column(db.String(256))
    text = db.Column(db.Text(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    photo = db.Column(db.Text(500))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)