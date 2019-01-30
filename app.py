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

<<<<<<< HEAD
@app.route('/names/yasmine')
def yasmine():
	return "I'm not ed. I'm Yasmine. :)" 

=======
@app.route('/names/Vivian')
def vivian():
    return "I'm Vivian"
    
>>>>>>> 04459f97653c9974a382b74ca367ba2fd43843d7
