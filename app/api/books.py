from flask import request, jsonify
from . import api_bp
from app import models
from app import db


@api_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify(models.Book.to_collection_json())

@api_bp.route('/books/', methods=['POST'])
def add_book():
    book = models.Book(**request.get_json())
    db.session.add(book)
    db.session.commit()
    return jsonify(**request.get_json())

@api_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return jsonify(models.Book.query.get_or_404(book_id).to_json())



