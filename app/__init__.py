import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Создание абсолютного пути к базе данных
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'clicker.db')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app.models import User  # Импортируем модель User после инициализации базы данных

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app import routes  # Импортируем маршруты после определения функции load_user
