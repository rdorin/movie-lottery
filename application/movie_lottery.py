from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.secret_key = b'^@toETAD94we\n\x81/'

db = SQLAlchemy(app)

# Setting up movie table
class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	movie_name = db.Column(db.String(50))


def authorized():
	if 'username' in session:
		return True
	else:
		return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		if 'N51RN' == request.form['username']:
			session['username'] = 'G2G'
			return redirect(url_for('index'))
	return render_template('login.html')


@app.route('/')
def index():
	is_authorized = authorized()
	if is_authorized is not True:
		return is_authorized;
	# return redirect(url_for('hello'))
	return render_template('index.html')

@app.route('/add')
def render_form(name=None):
	return render_template('add.html', name=name)

@app.route('/movie/add', methods=['POST'])
def add_movie():
	is_authorized = authorized()
	if is_authorized is not True:
		return is_authorized;
	if request.method == 'POST':
		mname = request.form.get('mname','')
		movie = Movie(movie_name=mname)
		db.session.add(movie)
		db.session.commit()

	return render_template('index.html')

@app.route('/movie/lottery')
def get_movie():
	movie = Movie.query.order_by(func.random()).first()
	return render_template('movie.html',name=movie.movie_name,id=movie.id)

@app.route('/movie/delete/<id>')
def del_movie(id):
	is_authorized = authorized()
	if is_authorized is not True:
		return is_authorized;
	movie = Movie.query.filter_by(id=id).first()
	if movie:
		db.session.delete(movie)
		db.session.commit()
	return render_template('index.html')

@app.route('/movie')
def get_movies():
	is_authorized = authorized()
	if is_authorized is not True:
		return is_authorized;
	movies = Movie.query.all()
	return render_template('list.html', movies=movies)