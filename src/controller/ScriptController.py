from flask import Blueprint, jsonify
import subprocess

script_api = Blueprint("script_api", __name__)


@script_api.route("/bash", methods=["POST"])
def index():
    subprocess.call(['/tmp/test.sh'])
    return jsonify({
        "success": True
    }), 201
