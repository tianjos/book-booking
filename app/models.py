from app import db


authors = db.Table('authors',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    books = db.relationship('Book', backref='publisher', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)
    authors = db.relationship('Author', secondary=authors, lazy='subquery', backref=db.backref('books', lazy=True))
