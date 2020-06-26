import os

import cli
from app import create_app


env = os.getenv('ENV', 'development')
app = create_app(env)
cli.register(app)
