import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('hello.html')

@app.route('/dino')
def dinosaur():
	return render_template('dino.html')

@app.route('/activities')
def act():
	return render_template('activities.html')
	
@app.route('/additionalinfo')
def addinfo():
	return render_template('addinfo.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')
	
@app.route('/mit')
@app.route('/MIT')
def MIT():
	return render_template('MIT.html')	
@app.route('/sigma')
def sig():
	#import scraper
	#scraper.make_graph()
	return render_template('cat.html',name='MALgraph.gexf')

@app.route('/college')
def col():
	#return 'hi'
	return render_template('cmain.html')

@app.route('/reader')
def reader():
	return render_template('reader.html')

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
