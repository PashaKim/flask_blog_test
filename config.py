import os


class Configuration:
    DEBUG = True
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    DATABASE = os.path.join(PROJECT_ROOT, 'tmp', 'flask_test.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

