from flask import request, jsonify
from . import api_bp
from app import models
from app import db


@api_bp.route('/authors', methods=['GET'])
def get_authors():
    return jsonify(models.Author.to_collection_json())
    
@api_bp.route('/authors/', methods=['POST'])
def add_author():
    author = models.Author(**request.get_json())
    db.session.add(author)
    db.session.commit()
    return jsonify(**request.get_json())

@api_bp.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    return jsonify(models.Author.query.get_or_404(author_id).to_json())



