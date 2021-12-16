import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    ROOT_PATH = basedir
    STATIC_FOLDER = os.path.join(basedir, 'app/view/static')
    TEMPLATE_FOLDER = os.path.join(basedir, 'app/view/templates')