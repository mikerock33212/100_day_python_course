from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('index.html', posts=all_posts)


@app.route('/post/<int:blog_id>')
def get_blog_post(blog_id):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog_post.html', posts=all_posts, blogid=blog_id)


if __name__ == "__main__":
    app.run(debug=True)
