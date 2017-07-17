from config.AppConfig import app
from flask import Blueprint, request, jsonify
from schema.AuthUser import AuthUser
from flask_bcrypt import Bcrypt
from service.AuthUserService import AppUserService
import jwt
import os

auth_api = Blueprint("authentication_api", __name__)
bcrypt = Bcrypt(app)
savedPass = ""
aus = AppUserService()


@auth_api.route("/register", methods=["POST"])
def register():
    auth_user_json = request.json
    data, errors = AuthUser().load(auth_user_json)
    if bool(errors):
        return jsonify(errors)
    auth_user = aus.getOneByName(auth_user_json['username'])
    if 'username' in auth_user:
        return jsonify({
            "success": False,
            "message": "username already exist"
        })
    pw_hash = bcrypt.generate_password_hash(auth_user_json['password'])
    data['password'] = pw_hash.decode('utf8')
    aus.create(data)
    return jsonify({
        "success": True
    }), 201


@auth_api.route("/login", methods=["POST"])
def login():
    auth_user_json = request.json
    data, errors = AuthUser().load(auth_user_json)
    if bool(errors):
        return jsonify(errors), 400

    auth_user = aus.getOneByName(auth_user_json['username'])
    if 'username' not in auth_user:
        return jsonify({
            "success": False,
            "message": "username not found"
        }), 400
    if bcrypt.check_password_hash(auth_user['password'], auth_user_json['password']):
        env_secret = os.getenv('FLASK_SECRET_KEY', '')
        if env_secret == '':
            return jsonify({
                "error": "server",
                "hint": "env_secret"
            })
        encoded = jwt.encode({'some': 'payload'}, env_secret, algorithm='HS256')
        return jsonify({
            "success": True,
            "token": encoded.decode('utf8')
        })
    else:
        return jsonify({
            "success": False,
            "message": "Username or Password incorrect"
        }), 400


@auth_api.route("/logout", methods=["POST"])
def logout():
    env_secret = os.getenv('FLASK_SECRET_KEY', '')
    if env_secret == '':
        return jsonify({
            "error": "server",
            "hint": "env_secret"
        })
    encoded = jwt.encode({'some': 'payload'}, env_secret, algorithm='HS256')

    return jsonify({
        "token": encoded.decode('utf8')
    })
