from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FloatField,HiddenField
from wtforms.validators import DataRequired
import requests


import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///mydata.db'
app.config['WTF_CSRF_ENABLED'] = False


app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
Bootstrap(app)
db = SQLAlchemy(app)
api_key = '0bfe7bcc76b7e9041b6493f5e89d3b10'

API_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
API_IMG_URL = 'https://image.tmdb.org/t/p/w500'
SELECTED_MOVIE = 'https://api.themoviedb.org/3/movie'

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(300))
    rating = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(300))
    img_url =db.Column(db.String(300))
    





@app.route("/")
def home():
    #movie = Movie.query.all()
    #movie list sorted by rating
    all_movies_sorted = Movie.query.order_by(Movie.rating.desc()).all()
    for indeks,movie in enumerate(all_movies_sorted):
        movie.ranking = indeks+1

    


    return render_template("index.html",temp_movie=all_movies_sorted)

@app.route('/edit', methods=['GET','POST'])
def rate_movie():
    form = MovieForm()
    movie_id = request.args.get('id')
    movie= db.session.get(Movie, movie_id)
    print(movie,'This is the movie user select')
            

    if form.validate_on_submit():
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        movie.rating = float(form.rating.data)
        movie.review= form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',temp_form=form,temp_movie=movie)

@app.route('/delete',methods=['GET','POST'])
def delete_movie():
    movie_id = request.args.get('id')
    movie= db.session.get(Movie, movie_id)

    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add',methods=['GET','POST'])
def add_movie():
    adform= addForm()

    if adform.validate_on_submit():
        movie_title = adform.title.data
        response = requests.get(API_SEARCH_URL,params={'api_key': api_key,'query':movie_title})
        data = response.json()['results']
        
        return render_template('select.html',temp_data = data)
    

    return render_template('add.html',temp_addform=adform)


@app.route('/find')
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_api_url = f'{SELECTED_MOVIE}/{movie_api_id}'
        response = requests.get(movie_api_url,params={'api_key': api_key})
        data = response.json()
        print(data)
        
        new_movie=Movie(
            title =data["title"],
            year =data['release_date'].split("-")[0],
            img_url=f"{API_IMG_URL}{data['poster_path']}",
            description= data['overview'] 
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('rate_movie',id=new_movie.id))
        



        







newMovie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)


class MovieForm(FlaskForm):
    rating = StringField('Your rating out of 10')
    review = StringField('Your Review')
    submit = SubmitField('Send')

class addForm(FlaskForm):
    
    title = StringField('Movie Title')
    submit = SubmitField('Submit')






































if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        
        app.run(debug=True)
        





