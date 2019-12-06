from app import app
from flask import json
from flask_cors import CORS

CORS(app)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/data')
def data():
    data = {"json":"data"}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
