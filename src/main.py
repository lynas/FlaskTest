from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from controller.AppUserController import app_user_api
from schema.UserSchema import UserSchema

app = Flask(__name__)
app.register_blueprint(app_user_api, url_prefix='/app_users')
app.config['MONGO_HOST'] = '127.0.0.1'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'flsk'
mongo = PyMongo(app, config_prefix='MONGO')


@app.route('/')
def index():
    return 'this is the homepage'



@app.route("/users", methods=['POST'])
def users():
    user_json = request.json
    data, errors = UserSchema().load(user_json)
    if bool(errors):
        return jsonify(errors)
    return jsonify(user_json)


if __name__ == "__main__":
    app.run(debug=True)
