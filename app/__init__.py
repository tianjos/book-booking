from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(env):
    app = Flask(__name__)
    
    return app
