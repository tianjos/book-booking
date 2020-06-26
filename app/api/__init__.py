from flask import Blueprint


api_bp = Blueprint('api', __name__)


from . import authors
from . import books
from . import publishers
