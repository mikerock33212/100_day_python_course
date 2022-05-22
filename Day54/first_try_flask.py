from flask import Flask

app = Flask(__name__)


def make_bold(end_points):
    def wrapper_func():
        return f'<b>{end_points()}</b>'
    return wrapper_func


def make_italic(end_points):
    def wrapper_func():
        return f'<em>{end_points()}</em>'
    return wrapper_func


def make_underline(end_points):
    def wrapper_func():
        return f'<u>{end_points()}</u>'
    return wrapper_func


@app.route('/')
@make_bold
@make_italic
@make_underline
def hello():
    return '<h1 style="text-align: center">Hello World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="" width='


if __name__ == '__main__':
    app.run(debug=True)

