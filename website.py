#!/usr/bin/env python3

#########################################################
# index.py
# Created by:  Kyle Hurd
# Modified:    12/01/2020
# Description: The main driver for Kyle Hurd's website.
#########################################################


# Imports
#########################################################
from flask import Flask, render_template, url_for
import ast

# Blueprints
#########################################################
from flappy_bird import flappy_bird
from projects import projects
from metar import metar


# App
#########################################################
app = Flask(__name__, template_folder = 'templates', static_folder = 'static')

app.register_blueprint(flappy_bird)
app.register_blueprint(projects)
app.register_blueprint(metar)


# Functions
#########################################################
# current_page can equal the following: 'Main', 'Projects',
#                                           'My Music', 'About Me'

# Home
@app.route('/')
def home_page():
    return render_template('main.html', current_page='Main')

@app.route('/projects/')
def projects():
    return render_template('projects.html', current_page='Projects')

@app.route('/my_music/')
def my_music():
    return render_template('my_music.html', current_page='My Music')

@app.route('/my_music/tabs/')
def tabs():
    try:
        f = app.open_resource('static/music_projects/songs.txt', 'r')
        content = f.read()
        playlist = ast.literal_eval(content)
    except:
        return 'Could not load tabs. Please try again later.'
    f.close()
    return render_template('tabs.html', playlist=playlist, current_page='Tabs')

@app.route('/about_me/')
def about_me():
    return render_template('about_me1.html', current_page='About Me')

# Override
@app.route('/<string:name>/')
def static_page(name):
    return render_template(f'templates/{name}.html')


# Run
########################################################
if __name__ == '__main__':
    debug = False
    app.run()
