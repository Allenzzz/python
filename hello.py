# -*- coding:utf-8 -*-
# hello.py


from flask import Flask
app = Flask(__name__)
# @app.route('/')
# def hello_world():
# 	return 'Hello world!'
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

if __name__=='__main__':
	# app.debug = True
	# app.run()
	# 另一种是作为参数传递给 run 方法:

	app.run(debug=True)
	# 两种方法的效果相同。