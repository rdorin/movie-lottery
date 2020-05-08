from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

# Setting up movie table
class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	movie_name = db.Column(db.String(50))

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
		movie = Movie(movie_name=mname)
		db.session.add(movie)
		db.session.commit()

	return "<h1>Added movie to the database!</h1>"

@app.route('/movie/lottery')
def get_movie():
	count = db.session.query(Movie).count()
	id = randint(1,count)
	movie = Movie.query.filter_by(id=id).first()
	return f"<h1>{ movie.movie_name }</h1>"
