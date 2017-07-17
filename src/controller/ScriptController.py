from flask import Blueprint, jsonify
import subprocess

script_api = Blueprint("script_api", __name__)


@script_api.route("/bash", methods=["POST"])
def bash():
    subprocess.call(['/tmp/test.sh'])
    return jsonify({
        "success": True
    })


@script_api.route("/perl", methods=["POST"])
def perl():
    subprocess.call(['/tmp/test.pl'])
    # subprocess.Popen(["perl", "/tmp/test.pl"])
    return jsonify({
        "success": True
    })
