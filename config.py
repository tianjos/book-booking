import os


class Config:
    DB_HOST = os.environ.get("DB_HOST")
    DB_PASS = os.environ.get("DB_PASS")
    DB_USER = os.environ.get("DB_USER")
    SECRET_KEY = os.environ.get("SECRET_KEY", 'my secret key here')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def init_app(self):
        pass

    @classmethod
    def make_db_url(cls, db_name: str):
        cls.SQLALCHEMY_DATABASE_URI = f"postgresql://{cls.DB_USER}:{cls.DB_PASS}@{cls.DB_HOST}/{db_name}"

class Development(Config):

    @staticmethod
    def init_app():
        Config.make_db_url('book-development')  

class Testing(Config):

    @staticmethod
    def init_app():
        Config.make_db_url('book-testing')

class Production(Config):
    pass


class Heroku(Production):
    '''Heroku Config'''
    @staticmethod
    def init_app():
        try:
            SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        except KeyError:
            raise EnvironmentError("MUST SET DATABASE_URL")

config = {
    'development': Development,
    'production': Production,
    'testing': Testing,
    'heroku': Heroku,
}
