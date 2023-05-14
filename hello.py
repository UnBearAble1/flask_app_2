from flask import Flask, render_template

# create an instance
app = Flask(__name__)

# create route
@app.route('/')

def index():
    return "<h1>Hello World</h1>"
