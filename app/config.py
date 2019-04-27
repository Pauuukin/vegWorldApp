import os


#----------------Postgresql----------------#
#
# POSTGRES = {
#     'user': 'postgres',
#     'pw': 'pass1234',
#     'db': 'my_database',
#     'host': 'localhost',
#     'port': '5432',
# }
# class Config(object):
#     '''Параметры конфигурации определяются как переменные класса внутри класса Config. '''
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#     # местоположение бд приложения
#     SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
#     # отключаемб чтобы не получать сигналы каждый разб когда в бд должно быть внесенно изменение
#     SQlALCHEMY_TRACK_MODIFICATION = True
# ----------------Postgresql----------------#



"""         sqlite          """
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Переменная конфигурации SECRET_KEY, которую я добавил как единственный элемент
# конфигурации, является важной частью большинства приложений Flask.
# Flask и некоторые его расширения используют значение секретного ключа в
# качестве криптографического ключа, полезного для генерации подписей или токенов.
# Значение секретного ключа задается как выражение с двумя терминами, к которым
# присоединяется оператор OR. Первый термин ищет значение переменной среды,
# также называемой SECRET_KEY. Второй термин, это просто жестко закодированная строка