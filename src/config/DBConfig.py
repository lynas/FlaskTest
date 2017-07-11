from flask import Flask
from flask_pymongo import PyMongo

application = Flask(__name__)
application.config['MONGO_HOST'] = '127.0.0.1'
application.config['MONGO_PORT'] = 27017
application.config['MONGO_DBNAME'] = 'flsk'
mongoDB = PyMongo(application, config_prefix='MONGO')
