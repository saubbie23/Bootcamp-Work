from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

books_author_collat = db.Table('collat', 
                      db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
                      db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True))

class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    authors_of_book = db.relationship('Authors', secondary=books_author_collat)

    def __repr__(self):
        return f"Book Id: {self.id}\nBook Title: {self.title}\nBook Description: {self.description}"

    def __str__(self):
        return f"Book Id: {self.id}\nBook Title: {self.title}\nBook Description: {self.description}"  

class Authors(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    notes = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    books_by_author = db.relationship('Books', secondary=books_author_collat)

    def __repr__(self):
        return f"Author Name: {self.first_name} {self.last_name}\nNotes: {self.notes}"

    def __str__(self):
        return f"Author Name: {self.first_name} {self.last_name}\nNotes: {self.notes}"

# Routes
@app.route('/')
def index():
    books = Books.query.all()
    return render_template('index.html', books=books)

### Book Routes ###
@app.route('/add_book', methods=['POST'])
def add_book():
    new_book = Books(title=request.form['title'], description=request.form['description'])
    db.session.add(new_book)
    db.session.commit()

    return redirect('/')

@app.route('/books/<id>')
def view_book(id):
    books = Books.query.get(id)
    authors = Authors.query.all()
    return render_template('view_book.html', book=books, authors=authors)

@app.route('/add_book_to_author', methods=['POST'])
def add_book_to_author():
    curr_book = Books.query.get(request.form['book_id'])
    curr_author = Authors.query.filter_by(first_name= request.form['author'])
    curr_author = Authors.query.get(curr_author[0].id)

    curr_book.authors_of_book.append(curr_author)
    db.session.commit()

    return redirect('/books/' + request.form['book_id'])


### Author Routes ###
@app.route('/authors')
def authors():
    authors = Authors.query.all()
    return render_template('authors.html', authors=authors)

@app.route('/add_author', methods=["POST"])
def add_author():
    new_author = Authors(first_name=request.form['first_name'], last_name=request.form['last_name'], notes= request.form['notes'])
    db.session.add(new_author)
    db.session.commit()

    return redirect('/authors')

@app.route('/authors/<id>')
def view_author(id):
    authors = Authors.query.get(id)
    books = Books.query.all()
    print(books)
    return render_template('view_author.html', author=authors, books=books)

@app.route('/add_author_to_book', methods=['POST'])
def add_author_to_book():
    curr_author = Authors.query.get(request.form['author_id'])
    curr_book = Books.query.filter_by(title=request.form['book'])
    curr_book = Books.query.get(curr_book[0].id)

    curr_author.books_by_author.append(curr_book)
    db.session.commit()

    return redirect('/authors/' + request.form['author_id'])

if __name__ == "__main__":
    app.run(debug=True)