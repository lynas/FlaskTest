from flask_classy import FlaskView, route, request
from flask import jsonify
from service.AppUserService import AppUserService
from schema.AppUser import AppUser


class AppUserController(FlaskView):
    def __init__(self):
        self.app_user_service = AppUserService()

    @route("/")
    def get_all(self):
        return jsonify(self.app_user_service.getAll())

    @route("/<first_name>")
    def get(self, first_name):
        return jsonify(self.app_user_service.getOneAppUserByName(first_name))

    @route("/", methods=["POST"])
    def create(self):
        app_user_json = request.json
        data, errors = AppUser().load(app_user_json)
        if bool(errors):
            return jsonify(errors)
        return jsonify(self.app_user_service.createNewAppUser(data)), 201

    @route("/<app_user_id>", methods=["PATCH"])
    def update(self, app_user_id):
        app_user_json = request.json
        data, errors = AppUser().load(app_user_json)
        if bool(errors):
            return jsonify(errors)
        result = self.app_user_service.updateAppUser(app_user_id, data)
        return jsonify(result)

    @route("/<app_user_id>", methods=["DELETE"])
    def delete(self, app_user_id):
        result = self.app_user_service.delete(app_user_id)
        return jsonify(result)
