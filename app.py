from flask import Flask
app = Flask(__name__)


@app.route('/names/Xoch')
def index():
    return "Xoch"

@app.route('/')
def index():
    return "Please create an endpoint with your name as the URL"
