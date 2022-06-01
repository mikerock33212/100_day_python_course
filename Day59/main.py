from flask import Flask, render_template, url_for, request
import requests
import datetime

app = Flask(__name__)

BLOG_URL = 'https://api.npoint.io/4d806cb1ec2694f83a5d'
CONTENTS = requests.get(BLOG_URL).json()
now = datetime.datetime.today()
NOW_DATE = now.strftime('%d/%m/%Y')


@app.route('/')
def home():
    return render_template('index.html', posts=CONTENTS, date=NOW_DATE)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["textarea"])
        return render_template('contact.html', msg_sent=True)
    return render_template("contact.html", msg_send=False)


@app.route('/post/<int:index>')
def show_post(index):
    requested_blog = CONTENTS[index - 1]
    return render_template('post.html', posts=requested_blog, date=NOW_DATE)


@app.route('/post')
def post_page():
    return render_template('post.html', posts=CONTENTS, date=NOW_DATE)


if __name__ == '__main__':
    app.run(debug=True)
