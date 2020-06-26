from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(env):
    cfg = config[env]
    cfg.init_app()
    
    app = Flask(__name__)
    app.config.from_object(cfg)

    db.init_app(app)

    return app
