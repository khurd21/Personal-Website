#!/usr/bin/env python3

import flask


from src.website import menu_bar_tabs
from src.metar_weather_data import metar_weather_data

app = flask.Flask(
        __name__,
        template_folder='templates',
        static_folder='static'
        )

app.register_blueprint(menu_bar_tabs)
app.register_blueprint(metar_weather_data)


if __name__ == '__main__':
    app.run(debug=False)
