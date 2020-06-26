from app import db


authors = db.Table('authors',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    @classmethod
    def to_collection_json(cls) -> list:
        authors = cls.query.filter_by().all()
        return [author.to_json() for author in authors]

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    books = db.relationship('Book', backref='publisher', lazy=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'books': self.books
        }

    @classmethod
    def to_collection_json(cls) -> list:
        publishers = cls.query.filter_by().all()
        return [publisher.to_json() for publisher in publishers]

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)
    authors = db.relationship('Author', secondary=authors, lazy='subquery', backref=db.backref('books', lazy=True))

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            # 'publisher': Publisher.query(id=self.publisher_id).to_json(),
            'publisher': self.publisher_id,
            'authors': self.authors
        }
    
    @classmethod
    def to_collection_json(cls) -> list:
        books = cls.query.filter_by().all()
        return [book.to_json() for book in books]
