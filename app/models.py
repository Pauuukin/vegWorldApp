from app import db

class User(db.Model):
    idUser = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    nickname = db.Column(db.String(32), unique = True)
    phoneNumber = db.Column(db.String(32), unique = True)
    password_hash = db.Column(db.String(128))
    gender = db.Column(db.String(32))
    aboutMe = db.Column(db.Text(600))
    dateOfBirth = db.Column(db.Date)

    def __repr__(self):
        """Сообщает, как печатать объект класса"""
        return '<User {}>'.format(self.nickname)