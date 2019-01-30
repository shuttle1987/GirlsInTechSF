##########################
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
<<<<<<< HEAD

<<<<<<< HEAD
@app.route('/names/yasmine')
def yasmine():
	return "I'm not ed. I'm Yasmine. :)" 

=======
@app.route('/names/Vivian')
def vivian():
    return "I'm Vivian"
    
>>>>>>> 04459f97653c9974a382b74ca367ba2fd43843d7
=======
  
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
>>>>>>> bddf8fa9bb932cf09f4289e64aa9be5c20827a9d
