#!usr/bin/env python3
#encoding: utf-8

from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.before_app_request()
def before_request():
    #connect to mysql database
    

@app.route('/users', methods = ['POST'])
def create_user():
    return "Product created!"

@app.route('/get-user/<user_id>', methods = ['GET'])
def get_user(user_id):
    return jsonify({'id': user_id, 'name': 'alex', 'email': 'alex@gmail.com'})


if __name__ == "__main__":
    
    app.run(host = '0.0.0.0', debug = True)
