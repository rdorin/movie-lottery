from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/')
def index():
	# return redirect(url_for('hello'))
	return render_template('index.html')

@app.route('/add')
def render_form(name=None):
	return render_template('add_form.html', name=name)

@app.route('/movie/add', methods=['POST'])
def add_movie():
	if request.method == 'POST':
		mname = request.form.get('mname','')
		return mname