from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(BASE_DIR, 'market.db')
#database_path = r'C:\Users\USER\sqlite\market.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
app.config['SECRET_KEY'] = 'aaa84d2a6a9b0215c9113cf5'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from . import routes
