import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('hello.html')

@app.route('/dino')
def dinosaur():
	return render_template('dino.html')

@app.route('/links')
def links():
	return render_template('links.html')

#@app.route('/css/<path:fnc>')
def css_static(fn):
	return send_from_directory('/css/',fnc)

#@app.route('/static/<path:fns>')
def static(fn):
	return send_from_directory('/static/',fns)

#@app.route('/js/<path:fnj>')
def js_static(fn):
	return send_from_directory(app.config['JS_STATIC'],fnj)



@app.route('/temp/<name>')
def temp(name=None):
	return render_template('display.html',name=name)

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000
	port = int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0',port=port,debug=True)
