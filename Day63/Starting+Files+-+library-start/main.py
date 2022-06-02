from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-book-collection.db'
app.secret_key = 'fdas123@!#@#'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>, <author {self.author}>, <rating {self.rating}>'


db.create_all()


# create record
# new_book = Book(id=1, title='Harry Potter', author='J.K. Rowling', rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# update a book by title
# book_to_update = Book.query.filter_by(title='Harry Potter').first()
# book_to_update.title = 'Harry Potter and the Chamber of Secrets'
# print(Book.query.all())

# update a record by ID
# book_to_update = Book.query.get(1)
# book_to_update.title = 'Harry Potter and the Goblet of Fire'
# print(Book.query.all())

# delete a particular record
# book_to_delete = Book.query.get(1)
# db.session.delete(book_to_delete)
# db.session.commit()
# print(Book.query.all())


# sqlite method
# db = sqlite3.connect('books_collection.db')
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


@app.route('/')
def home():
    all_books = []
    temp_dict = {}
    for item in Book.query.all():
        temp_dict['id'] = item.id
        temp_dict['title'] = item.title
        temp_dict['author'] = item.author
        temp_dict['rating'] = item.rating
        all_books.append(temp_dict)
        temp_dict = {}
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['book_name']
        author = request.form['author']
        rating = request.form['rating']
        # temp_book_dic = {'title': book_name,
        #                  'author': author,
        #                  'rating': rating}
        # all_books.append(temp_book_dic)
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id_ = request.args.get('id')
    book_selected = Book.query.get(book_id_)
    return render_template('edit.html', book=book_selected)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    db.session.delete(book_selected)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

