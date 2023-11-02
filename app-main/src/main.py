#!/usr/bin/env python3
# encoding: utf-8
import json
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return jsonify({'name': 'alex',
                       'email': 'alex@gmail.com',
                       'id': 1})

@app.route('/users-info', methods = ['GET'])
def users_info():
    return jsonify({'users': 'all_users'})

@app.route('/user/<user_id>', methods = ['GET'])
def user_data(user_id):
    if request.method == 'GET':
        #Request to auth service to get user data
        session = requests.Session()
        session.trust_env = False
        try:
            data = session.get(f'http://auth:5000/get-user/{user_id}') 
        except Exception as e:
            return jsonify({'error': str(e)})              

        return jsonify({'name': data.json()['name'],
                       'email': data.json()['email']})
    elif request.method == 'POST':
        #Request to auth to create new user 
        return jsonify({'name': name, 'email': email})
    else:
        return jsonify({'error': 'Method not allowed'})


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)

