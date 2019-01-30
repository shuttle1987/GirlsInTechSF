"""This is a an example of a Flask app"""

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
    return "I'm Ed"
  
@app.route('/names/annie')
def annie():
    return "Annie"

@app.route('/names/Irene')
def irene():
    return "I'm Irene"


@app.route('/names/meghana')
def meghana():
    return "I'm Meghana"



@app.route('/names/rajasree')
def rajasree():
    return "I'm Rajasree"

@app.route('/names/Xoch')
def ed():
    return "Xoch"
  
@app.route('/gitbranchexample')
def branch_example():
    return "This was done on a git branch"


@app.route('/names/Vivian')
def vivian():
    return "I'm Vivian"