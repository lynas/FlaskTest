from flask import Blueprint, request, jsonify
from service.AppUserService import AppUserService
from schema.AppUser import AppUser

app_user_api = Blueprint("app_user_api", __name__)
aus = AppUserService()


@app_user_api.route("/")
def getAll():
    return jsonify(aus.getAll())


@app_user_api.route("/<firstName>")
def get(firstName):
    return jsonify(aus.getOneAppUserByName(firstName))


@app_user_api.route("/", methods=["POST"])
def create():
    app_user_json = request.json
    data, errors = AppUser().load(app_user_json)
    if bool(errors):
        return jsonify(errors)
    return jsonify(aus.createNewAppUser(data)), 201


@app_user_api.route("/<app_user_id>", methods=["PATCH"])
def update(app_user_id):
    app_user_json = request.json
    data, errors = AppUser().load(app_user_json)
    if bool(errors):
        return jsonify(errors)
    result = aus.updateAppUser(app_user_id, data)
    return jsonify(result)


@app_user_api.route("/<app_user_id>", methods=["DELETE"])
def delete(app_user_id):
    result = aus.delete(app_user_id)
    return jsonify(result)
