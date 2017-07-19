from flask import Flask
from flask import request, jsonify
from flask_pymongo import PyMongo
from controller.AppUserController import app_user_api
from controller.AuthenticationController import auth_api
from controller.ScriptController import script_api
from schema.UserSchema import UserSchema
from Util import decode_auth_token

app = Flask(__name__)
app.config['MONGO_HOST'] = '127.0.0.1'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'flsk'
app.register_blueprint(app_user_api, url_prefix='/app_users')
app.register_blueprint(auth_api, url_prefix='/auth')
app.register_blueprint(script_api, url_prefix='/script')
dbCon = PyMongo(app)


@app.route('/')
def index():
    return jsonify({
        "success": True
    })


@app.route("/users", methods=['POST'])
def users():
    user_json = request.json
    data, errors = UserSchema().load(user_json)
    if bool(errors):
        return jsonify(errors)
    return jsonify(user_json)


@app.before_request
def before_request():
    if request.path.startswith('/app_users'):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Authentication error"})
        else:
            success, message = decode_auth_token(token)
            if not success:
                return jsonify({"error": "Authentication error", "message": message})


if __name__ == "__main__":
    app.run(debug=True)
