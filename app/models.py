from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin
from app import login

#таблица ассоциаций фоловеров
followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
                     )
#таблица пользователей
class User(UserMixin, db.Model):
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
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    #много ко многим
    followed = db.relationship(
        'User', secondary=followers,                    #кофигурирует таблицу ассоциаций, которая используется
                                                        # для этой связи, которую я определил прямо над этим классом.
        primaryjoin = (followers.c.follower_id == id),  #указывает условие, которое связывает объект
                                                        # левой стороны (follower user) с таблицей ассоциаций.
        secondaryjoin = (followers.c.followed_id == id),#определяет условие, которое связывает объект правой
                                                        # стороны (followed user) с таблицей ассоциаций.
        backref = db.backref('followers', lazy = 'dynamic'), lazy = 'dynamic'
        #backref определяет, как эта связь будет доступна из правой части объекта.
        # С левой стороны отношения пользователи называются followed, поэтому с правой стороны
        # я буду использовать имя followers, чтобы представить всех пользователей левой стороны,
        # которые связаны с целевым пользователем в правой части.
    )
    #followers.c.follower_id «c» — это атрибут таблиц SQLAlchemy, которые
    # не определены как модели. Для этих таблиц столбцы таблицы
    # отображаются как субатрибуты этого атрибута «c».

    def __repr__(self):
        """Сообщает, как печатать объект класса"""
        return '<User {}>'.format(self.nickname)

    def set_password(self, password):
        """хешируем пароль"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """проверяем пароль"""
        return check_password_hash(self.password_hash, password)

    def follow(self, user):
        """добавляем подписчика"""
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        """удаляем подписчика"""
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        """проверка на существование отношения"""
        return self.followed.filter(followers.c.followed_id == user.id).count()>0

    def followed_posts(self):
        """вернет все посты юзеров, на которых подписан потльзователь + сообщения самого пользователя"""
        followed = Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(
                                    followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id = self.id)
        return followed.union(own).order_by(Post.timestamp.desc())



#таблица категорий
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    parent_id = db.Column(db.Integer)
    posts = db.relationship('Post', backref='category', lazy='dynamic')


    def __repr__(self):
        """Сообщает, как печатать объект класса"""
        return 'Category {}'.format(self.name)

#таблица статусов
class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    text = db.Column(db.Text(500))
    posts = db.relationship('Post', backref='status', lazy='dynamic')

    def __repr__(self):
        """Сообщает, как печатать объект класса"""
        return 'Status {}'.format(self.title)


#таблица постов
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    headline = db.Column(db.String(256))
    text = db.Column(db.Text(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    photo = db.Column(db.Text(500))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)

    def __repr__(self):
        """Сообщает, как печатать объект класса"""
        return 'Status {}'.format(self.text)



@login.user_loader
def load_user(id):
    """загрузчик пользователя"""
    return User.query.get(int(id))

