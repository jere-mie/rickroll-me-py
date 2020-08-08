from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

with open('secrets.json') as f:
  data = json.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = data['secret_key']

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from website import routes