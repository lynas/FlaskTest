from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from controller.AppUserController import app_user_api
from schema.UserSchema import UserSchema
from config.DBConfig import dbConfig

app = Flask(__name__)
app.register_blueprint(app_user_api, url_prefix='/app_users')
dbConfig(app)

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
