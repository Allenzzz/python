from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
# def index():
# 	return 'Hello,world!'
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
    	title = 'Home',
    	user = user)