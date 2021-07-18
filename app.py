from flask import Flask, render_template, sessions, session
import pymongo
from flask.json import jsonify

app=Flask(__name__)
app.secret_key=b'\x15\xa3\xb3\x199Y7\xd8\xd0\xd1f\x1aP\xae\x90\xbf'
#Database
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.user_login_system
# client = pymongo.MongoClient('127.0.0.1', 27017)
# database = client["local"]
# collection = database["users"]


#Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

from user.models import session

@app.route('/dashboard/')
def dashboard():
    if('logged_in' in session):
        return render_template('dashboard.html')
    return render_template('home.html')
