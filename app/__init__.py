from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config


db = SQLAlchemy()
migrate = Migrate()


def create_app(env):
    cfg = config[env]
    cfg.init_app()
    
    app = Flask(__name__)
    app.config.from_object(cfg)

    db.init_app(app)
    migrate.init_app(app, db)

    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


from . import models
