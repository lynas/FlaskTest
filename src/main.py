from flask import Flask

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


if __name__ == "__main__":
    app.run(debug=True)
