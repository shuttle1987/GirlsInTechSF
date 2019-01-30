from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Please create an endpoint with your name as the URL"
    @app.route('/names/Namibia'):
     def Namibia():
         return "Cheers, I'm Namibia!"
