from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import sqlite3
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# try:
#     cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# except:
#     print("Database already exists")

# cursor.execute("INSERT OR IGNORE INTO books VALUES(1,'HarryPotter','J.K Rowling', 5.5)")
# db.commit()

class books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(120), nullable = False, unique = True)
    author_name = db.Column(db.String(80), nullable = False)
    rating = db.Column(db.Float, nullable = False)

db.create_all()
# entry = books(id = 1, book_name = "Harry Potter", author_name = "J.K Rowling", rating= 9.3)
# db.session.add(entry)
# db.session.commit()



all_books = []


@app.route('/')
def home():
    global all_books
    all_books = db.session.query(books).all()
    return render_template('index.html', b = all_books, length = len(all_books))


@app.route("/add", methods = ['POST', 'GET'])
def add():
    if request.method == 'POST':
        bn = request.form['bname']
        an = request.form['aname']
        r = request.form['rating']
        entry = books(book_name = bn, author_name = an, rating = r)
        db.session.add(entry)
        db.session.commit()
    #     all_books.append(t)
    # print(all_books)
    return render_template('add.html')



if __name__ == "__main__":
    app.run(debug=True)

