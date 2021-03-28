#########################################################
# flappy_bird.py
# Created by:  Kyle Hurd
# Modified:    12/01/2020
# Description: Driver for the source_files html files
#########################################################


# Imports
#########################################################
from flask import Blueprint, render_template, url_for

flappy_bird = Blueprint('flappy_bird', __name__)
#########################################################


# Functions
#########################################################


# Flappy Bird
########################################################


# Main Page
@flappy_bird.route('/flappy_bird/')
def main_page():
    return render_template('flappy_bird.html', current_page='Projects')
    
    
# Main Function
@flappy_bird.route('/flappy_bird/flappy_home/')
def main_function():
    return render_template('flappy_bird/flappy_home.html')
    

# Helper Functions
@flappy_bird.route('/flappy_bird/helper_functions/')
def helper_functions():
    return render_template('flappy_bird/helper_functions.html')
    
    
# Menu Scene
@flappy_bird.route('/flappy_bird/menu_scene/')
def menu_scene():
    return render_template('flappy_bird/menu_scene.html')
    
    
# Change Name Scene
@flappy_bird.route('/flappy_bird/change_name_scene/')
def change_name_scene():
    return render_template('flappy_bird/change_name_scene.html')
    
    
# High Score Scene
@flappy_bird.route('/flappy_bird/high_score_scene/')
def high_score_scene():
    return render_template('flappy_bird/high_score_scene.html')


# Game Scene
@flappy_bird.route('/flappy_bird/game_scene/')
def game_scene():
    return render_template('flappy_bird/game_scene.html')
    
    
# Loading Scene
@flappy_bird.route('/flappy_bird/loading_scene/')
def loading_scene():
    return render_template('flappy_bird/loading_scene.html')
    
    
# Bird Class
@flappy_bird.route('/flappy_bird/bird_class/')
def bird_class():
    return render_template('flappy_bird/bird_class.html')


# Pipe Class
@flappy_bird.route('/flappy_bird/pipe_class/')
def pipe_class():
    return render_template('flappy_bird/pipe_class.html')
