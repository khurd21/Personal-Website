from flask import Flask
from config import Config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from app.model import Base

Session = sessionmaker()
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

Session.configure(bind=engine)
session = Session()

def create_app(config=Config):

    global engine

    flask_app = Flask(__name__)
    flask_app.config.from_object(config)
    flask_app.static_folder = config.STATIC_FOLDER
    flask_app.template_folder = config.TEMPLATE_FOLDER

    Base.metadata.create_all(engine)

    from app.controller.routes.website import menu_bar_tabs
    from app.controller.routes.auth_routes import auth_routes
    from app.controller.routes.metar_weather_data import metar_weather_data

    flask_app.register_blueprint(menu_bar_tabs)
    flask_app.register_blueprint(auth_routes)
    flask_app.register_blueprint(metar_weather_data)

    return flask_app