########################################################
# projects.py
# Created by:  Kyle Hurd
# Modified:    12/01/2020
# Description: Driver for the projects html files
#########################################################


# Imports
#########################################################
from flask import Blueprint, render_template, url_for

projects = Blueprint('projects', __name__)
#########################################################


# Functions
#########################################################


# Basic Helper Functions
@projects.route('/projects/helper_functions/')
def basic_helper_functions():
    return render_template('projects/helper_functions.html')

# BST
@projects.route('/projects/BST/')
def BST():
    return render_template('projects/BST.html')
    
   
# Linked List
@projects.route('/projects/linked_list/')
def linked_list():
    return render_template('projects/linked_list.html')


# Queue
@projects.route('/projects/queue/')
def queue():
    return render_template('projects/queue.html')
    

# Sorting
@projects.route('/projects/sorting/')
def sorting():
    return render_template('projects/sorting.html')
    
   
# Stack
@projects.route('/projects/stack/')
def stack():
    return render_template('projects/stack.html')
