from flask import Blueprint, request, jsonify
from service.AppUserService import *
from schema.AppUser import AppUser

app_user_api = Blueprint("app_user_api", __name__)


@app_user_api.route("/")
def appUserList():
    return jsonify(getAppUserList())


@app_user_api.route("/<firstName>")
def getAppUser(firstName):
    return jsonify(getOneAppUserByName(firstName))


@app_user_api.route("/", methods=["POST"])
def createAppUser():
    app_user_json = request.json
    data, errors = AppUser().load(app_user_json)
    if bool(errors):
        return jsonify(errors)
    return jsonify(createNewAppUser(data)), 201


@app_user_api.route("/<app_user_id>", methods=["PATCH"])
def updateUser(app_user_id):
    app_user_json = request.json
    data, errors = AppUser().load(app_user_json)
    if bool(errors):
        return jsonify(errors)
    result = updateAppUser(app_user_id, data)
    return jsonify(result)
