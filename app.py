"""This is an example flask app
designed to show some features of GitHub"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Please create an endpoint with your name as the URL"

@app.route('/names/Sujatha/')
def sujatha():
    return "Sujatha is working on ToySharing project"

@app.route('/names/Sujatha/')
def sujatha():
    return "Sujatha is working on ToySharing project"


@app.route('/names/ed')
def ed():
    return "I'm Ed"
@app.route('/names/yasmine')
def yasmine():
	return "I'm not ed. I'm Yasmine. :)" 

@app.route('/names/Vivian')
def vivian():
    return "I'm Vivian"
      
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
def xoch():
    return "Xoch"
  
@app.route('/gitbranchexample')
def branch_example():
    return "This was done on a git branch"


@app.route('/names/Vivian')
def vivian():
    return "I'm Vivian"

@app.route('/names/Senay')
def Senay():
    return "I'm Senay. I am originally from Istanbul/Turkey. I live in SF and i like here a lot. I am learning git today. It is so much fun "
