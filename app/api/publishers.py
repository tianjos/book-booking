from flask import request, jsonify
from . import api_bp
from app import models
from app import db


@api_bp.route('/publishers', methods=['GET'])
def get_publishers():
    return jsonify(models.Publisher.to_collection_json())
    
@api_bp.route('/publishers/', methods=['POST'])
def add_publisher():
    publisher = models.Publisher(**request.get_json())
    db.session.add(publisher)
    db.session.commit()
    return jsonify(**request.get_json())

@api_bp.route('/publishers/<int:publisher_id>', methods=['GET'])
def get_publisher(publisher_id):
    return jsonify(models.Publisher.query.get_or_404(publisher_id).to_json())



