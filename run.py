from app import app, db
from  app.models import User, Post


app.debug = 'True'

@app.shell_context_processor
def make_shell_context():
    """создаем контекст оболочки, который добавляет экземпляр и модель бд в сеанс"""
    return {'db':db, 'User': User, 'Post': Post}
