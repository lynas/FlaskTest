from flask import Flask, request, jsonify
from marshmallow import Schema, fields, validate
from flask_pymongo import PyMongo
from controller.AppUserController import app_user_api
from schema.UserSchema import UserSchema

app = Flask(__name__)
app.register_blueprint(app_user_api, url_prefix='/app_users')
app.config['MONGO_HOST'] = '127.0.0.1'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'flsk'
mongo = PyMongo(app, config_prefix='MONGO')


@app.route('/db')
def db():
    output = []
    for q in mongo.db.AppUser.find():
        output.append({'firstName': q['firstName']})
    print("")
    return 'this is the homepage %s' % len(output)


@app.route('/')
def index():
    return 'this is the homepage'


@app.route("/profile/<username>")
def profile(username):
    return "hey %s" % username


@app.route("/num/<int:postId>")
def getNumber(postId):
    return "posted Number %s" % postId


@app.route("/postTest", methods=['POST'])
def postTest():
    return "Post method Test"


@app.route("/newPost", methods=['POST'])
def newPost():
    language = {"name": request.json['name']}
    return jsonify({"List": language})


@app.route("/users", methods=['POST'])
def users():
    user_json = request.json
    data, errors = UserSchema().load(user_json)
    print(data)
    print(errors)
    return jsonify(user_json)


if __name__ == "__main__":
    app.run(debug=True)
