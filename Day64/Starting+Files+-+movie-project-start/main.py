from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///New_Movies.db'
db = SQLAlchemy(app)

MOVIE_REQUEST_URL = 'https://api.themoviedb.org/3/search/movie'
API_KEY = 'd69f963bf7e4cdc1c99f790e06551535'

# create movie table in DB


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.String(250))
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'Movie <{self.title}>'


# create form object for updating movies in DB
class MovieForm(FlaskForm):
    ratings = FloatField(label='Your Rating Out of 10, e.g. 6.5', validators=[DataRequired()])
    reviews = StringField(label='Your Review of this Movie', validators=[DataRequired(), Length(min=5, max=100)])
    submit = SubmitField(label='OK to submit')


class AddMovie(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired(), Length(min=5, max=50)])
    submit = SubmitField(label='Add Movie')


db.create_all()
#
# new_movie = Movie(
#     title='Phone Booth',
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped "
#                 "in a phone booth, pinned down by an extortionist's sniper rifle. "
#                 "Unable to leave or receive outside help, Stuart's negotiation with "
#                 "the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    movie_obj = Movie.query.order_by(Movie.rating.desc()).all()
    for movie in range(len(movie_obj)):
        movie_obj[movie].ranking = movie + 1
        db.session.commit()
    return render_template("index.html", movies=movie_obj)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form_ = MovieForm()
    id_ = request.args.get('movie_id')
    current_movie_obj = Movie.query.get(id_)
    if form_.validate_on_submit():
        current_movie_obj.rating = form_.ratings.data
        current_movie_obj.review = form_.reviews.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=current_movie_obj, form=form_)


@app.route('/delete')
def delete():
    id_ = request.args.get('movie_id')
    movie_to_delete = Movie.query.get(id_)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.title.data
        parameters = {
            'api_key': API_KEY,
            'query': movie_title
        }
        response = requests.get(MOVIE_REQUEST_URL, parameters).json()
        # movie_description = []
        # movie_image_url = []
        # image_former_url = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/'
        movie_data = response['results']
        return render_template('select.html', form=form, movie_data=movie_data)
        # description=movie_description, image_url=movie_image_url
    return render_template('add.html', form=form)


@app.route('/get_movie_detail', methods=['GET', 'POST'])
def get_movie_detail():
    id_ = request.args.get('movie_id')
    if id_:
        movie_api_url = f"{'https://api.themoviedb.org/3/movie'}/{id_}"
        # The language parameter is optional, if you were making the website for a different audience
        # e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data['title'],
            year=data['release_date'].split('-')[0],
            description=data['overview'],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}")
        db.session.add(new_movie)
        db.session.commit()
        form_ = MovieForm()
        current_movie_obj = Movie.query.filter_by(title=data['title']).first()
        movie_id = current_movie_obj.id
        return redirect(url_for('edit', movie_id=movie_id, form=form_))


if __name__ == '__main__':
    app.run(debug=True)
