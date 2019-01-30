from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Please create an endpoint with your name as the URL"

@app.route('/name/kaye')
def kaye():
    return "Hi, this is Kaye"
