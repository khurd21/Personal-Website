from flask import Flask
from config import Config

def create_app(config=Config):

    flask_app = Flask(__name__)
    flask_app.config.from_object(config)
    flask_app.static_folder = config.STATIC_FOLDER
    flask_app.template_folder = config.TEMPLATE_FOLDER

    from app.controller.routes.website import menu_bar_tabs
    from app.controller.routes.metar_weather_data import metar_weather_data

    flask_app.register_blueprint(menu_bar_tabs)
    flask_app.register_blueprint(metar_weather_data)

    return flask_app