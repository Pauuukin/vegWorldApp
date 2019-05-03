from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)
app.config.from_object(Config)
#объект бд
db = SQLAlchemy(app)
#объект, представляющий механизм миграции
migrate = Migrate (app, db)

# login должно запрещать незареганным пользователям доступ к определенным функциям
# для этого перед названием функции нужно жобавить декоратор @login_required

login = LoginManager(app)
login.login_view = 'login'


from app import routes, models


# Сценарий выше просто создает объект приложения как экземпляр класса Flask,
# импортированного из пакета flask. Переменная __name__, переданная в класс Flask,
# является предопределенной переменной Python, которая задается именем модуля,
# в котором она используется. Flask использует расположение модуля, переданного
# здесь как отправную точку, когда ему необходимо загрузить связанные ресурсы