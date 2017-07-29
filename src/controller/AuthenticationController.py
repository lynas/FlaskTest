from flask import request, jsonify
from schema.AuthUser import AuthUser
from flask_bcrypt import Bcrypt
from service.AuthUserService import AppUserService
from service.TokenBlackListService import TokenBlackListService
from Util import encode_auth_token, decode_auth_token
from injector import inject
from flask_classy import FlaskView, route


class AuthenticationController(FlaskView):
    @inject
    def __init__(self):
        self.bcrypt = Bcrypt()
        self.savedPass = ""
        self.aus = AppUserService()
        self.tbs = TokenBlackListService()

    @route("/register", methods=["POST"])
    def registers(self):
        auth_user_json = request.json
        data, errors = AuthUser().load(auth_user_json)
        if bool(errors):
            return jsonify(errors)
        auth_user = self.aus.getOneByName(auth_user_json['username'])
        if 'username' in auth_user:
            return jsonify({
                "success": False,
                "message": "username already exist"
            })
        pw_hash = self.bcrypt.generate_password_hash(auth_user_json['password'])
        data['password'] = pw_hash.decode('utf8')
        self.aus.create(data)
        return jsonify({
            "success": True
        }), 201

    @route("/login", methods=["POST"])
    def login(self):
        auth_user_json = request.json
        data, errors = AuthUser().load(auth_user_json)
        if bool(errors):
            return jsonify(errors), 405

        auth_user = self.aus.getOneByName(auth_user_json['username'])
        if 'username' not in auth_user:
            return jsonify({
                "success": False,
                "message": "username not found"
            }), 400
        if self.bcrypt.check_password_hash(auth_user['password'], auth_user_json['password']):
            success, message = encode_auth_token()
            if not success:
                return jsonify({
                    "success": False,
                    "token": "Server error env_secret"
                })
            return jsonify({
                "success": True,
                "token": message
            })
        else:
            return jsonify({
                "success": False,
                "message": "Username or Password incorrect"
            }), 400

    @route("/logout", methods=["POST"])
    def logout(self):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({
                "Error": "Authorization"
            })
        else:
            success, message = decode_auth_token(token)
            if not success:
                return jsonify({
                    "Error": message
                })
            else:
                self.tbs.addToTokenBlackList(token)
                return jsonify({
                    "success": True,
                    "message": "Logout successful!"
                })
