from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
	return redirect(url_for('hello'))

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello/hello.html', name=name)