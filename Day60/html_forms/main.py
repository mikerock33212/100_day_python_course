from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        return render_template('login.html', user=user_name, password=password, sent=True)
    return render_template('login.html', sent=False)


if __name__ == '__main__':
    app.run(debug=True)
