from flask import Flask, request, jsonify
from marshmallow import Schema, fields, validate
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_HOST'] = '127.0.0.1'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'flsk'
mongo = PyMongo(app, config_prefix='MONGO')


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(
        required=True,
        error_messages={'required': 'Age is required.'}
    )
    city = fields.String(
        required=True,
        error_messages={'required': {'message': 'City required', 'code': 400}}
    )
    email = fields.Str(required=True,
                       validate=validate.Email(error='Not a valid email address'))


userSchema = UserSchema()


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
    userSchema.load(user_json)
    return jsonify(user_json)


if __name__ == "__main__":
    app.run(debug=True)
