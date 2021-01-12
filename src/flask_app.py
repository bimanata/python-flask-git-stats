import base64
import os
import sys
from flask import (Flask, jsonify, redirect, request, send_file,
                   send_from_directory, url_for, Response)
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, reqparse
import json

from util.backend import list_process
from config import app_port

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../'))
app = Flask(__name__)
CORS(app)

@app.route('/api/healthcheck', methods=['GET'])
def healthcheck():
    return "application is running"

@app.route('/api/git_status', methods=['POST'])
def check_git():
    auth_key = request.headers.get('Authorization')
    reqs = request.json['repository']
    output = request.json['output']

    result = {}

    if len(reqs) < 1:
        result['message'] = 'dont put empty list in repository list'

        return result
    
    else:

        returns = list_process(reqs,output)
        result['message'] = returns

        return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app_port,threaded=True)
  