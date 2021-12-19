import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ROOT_PATH = basedir
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(ROOT_PATH, 'website.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = os.path.join(ROOT_PATH, 'app/view/static')
    TEMPLATE_FOLDER = os.path.join(ROOT_PATH, 'app/view/templates')