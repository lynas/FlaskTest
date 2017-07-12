from flask import Flask
from flask_pymongo import PyMongo

application = Flask(__name__)


def dbConfig(app):
    app.config['MONGO_HOST'] = '127.0.0.1'
    app.config['MONGO_PORT'] = 27017
    app.config['MONGO_DBNAME'] = 'flsk'


dbConfig(application)
mongoDB = PyMongo(application, config_prefix='MONGO')
