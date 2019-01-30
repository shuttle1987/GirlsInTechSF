from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Please create an endpoint with your name as the URL"


@app.route('/names/Sujatha/')
def sujatha():
    return "Sujatha is working on ToySharing project"


@app.route('/names/ed')
def ed():
    return "I'm Senay Yakut. I am originally from Istanbul/Turkey. I live in SF and i like here a lot. I am learning git today. It is so much fun "
