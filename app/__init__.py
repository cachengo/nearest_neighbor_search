import os

from annoy import AnnoyIndex
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ann_ix = AnnoyIndex(app.config['ANN_INDEX_LENGTH'])
if os.path.isfile(app.config['ANN_INDEX_PATH']):
    ann_ix.load(app.config['ANN_INDEX_PATH'])

from app import views
