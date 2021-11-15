from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from flask_login import LoginManager

with open('config.json') as f:
  data = json.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = data['secret_key']

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# setting up login stuff
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from website import routes