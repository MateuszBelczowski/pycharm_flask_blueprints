from flask import Flask
from blueprint_example import bp

app = Flask(__name__)
app.register_blueprint(bp)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
