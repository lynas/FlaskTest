from flask import Blueprint, request, jsonify
from service.AppUserService import getAppUserList
from service.AppUserService import getOneAppUserByName

app_user_api = Blueprint("app_user_api", __name__)


@app_user_api.route("/")
def appUserList():
    return jsonify(getAppUserList())


@app_user_api.route("/<firstName>")
def getAppUser(firstName):
    return jsonify(getOneAppUserByName(firstName))


@app_user_api.route("/", methods=["POST"])
def createAppUser():
    message = {"message": "AppUser create success"}
    return jsonify(message)
