from flask import Flask
from datetime import datetime
from msrest.authentication import TopicCredentials
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"