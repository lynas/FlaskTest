from flask import Flask, request, jsonify

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
