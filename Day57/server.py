from flask import Flask, render_template
import random
import datetime
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    year_now = datetime.datetime.now().year
    random_num = random.randint(1, 10)
    return render_template('index.html', nu=random_num, year=year_now)


@app.route('/guess/<username>')
def guess(username):
    parameters = {
        'name': username
    }
    gender_contents = requests.get('https://api.genderize.io', params=parameters).content
    age_contents = requests.get('https://api.agify.io', params=parameters).content
    user_age = json.loads(age_contents.decode('utf-8'))['age']
    user_gender = json.loads(gender_contents.decode('utf-8'))['gender']
    return render_template('guess.html', user=username, gen=user_gender, age=user_age)


@app.route('/blog/<blog_id>')
def blog(blog_id):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)