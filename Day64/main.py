from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy import Column, String, Integer, Float
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = ''  # App secrete key
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"  # Setting the name of the database
# Initializing the database
db = SQLAlchemy(app)
Bootstrap5(app)  # Adding bootstrap to the app


class Movies(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(db.String(250), unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(String(250), nullable=False)
    rating = Column(Float, nullable=False)
    ranking = Column(Integer, nullable=False)
    review = Column(String(250), nullable=False)
    img_url = Column(String(250), nullable=False)


class EditMovie(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 e.g 8.5", validators=[DataRequired()])
    ranking = StringField(label="What would you rank this movie in your list", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    done = SubmitField(label="Done")


class AddMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    add = SubmitField(label="Add Movie")


with app.app_context():
    db.create_all()


def search_by_name(search):
    url = f"https://api.themoviedb.org/3/search/movie?query={search}&include_adult=true&language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": ""
    }

    response = requests.get(url, headers=headers)

    return response.json()

def search_by_id(search):
    url = f"https://api.themoviedb.org/3/movie/{search}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": ""
    }

    response = requests.get(url, headers=headers)

    return response.json()


@app.route("/")
def home():
    all_movies = Movies.query.order_by(Movies.ranking).all()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/int:<num>", methods=["GET", "POST"])
def edit(num):
    form = EditMovie()
    if form.validate_on_submit():
        movie_to_edit = Movies.query.get(num)
        movie_to_edit.rating = form.rating.data
        movie_to_edit.review = form.review.data
        movie_to_edit.ranking = form.ranking.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)


@app.route("/delete/int:<num>")
def delete(num):
    movie_to_delete = Movies.query.get(num)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        search = form.title.data
        return redirect(url_for('select', search=search))
    return render_template("add.html", form=form)


@app.route("/select/str:<search>")
def select(search):
    result = search_by_name(search)
    return render_template("select.html", movies=result["results"])


@app.route('/add_movie/<search>')
def add_movie(search):
    new_movie = search_by_id(search)
    movie_to_add = Movies(
        title=new_movie["original_title"],
        year=new_movie["release_date"].split("-")[0],
        description=new_movie["overview"],
        rating=0,
        ranking=0,
        review=" ",
        img_url=f"https://image.tmdb.org/t/p/w500{new_movie['poster_path']}"
    )
    db.session.add(movie_to_add)
    db.session.commit()
    movie_to_edit = Movies.query.filter_by(title=movie_to_add.title).first()
    return redirect(url_for('edit', num=movie_to_edit.id))


if __name__ == '__main__':
    app.run(debug=True)
