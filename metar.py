

########################################################
# Created by:  Kyle Hurd
# Modified:    03/25/2021
# File: metar.py
# Description: Controls metar data
#########################################################

from flask import Blueprint, render_template, url_for
import metar_logic as ml
import xml.etree.ElementTree as element_tree

metar = Blueprint('metar', __name__)

@metar.route('/projects/metar/')
def metar_default(name='KSHN-KBFI-KPUW-KHQM'):
    airports = list(name.split('-'))
    content = ml.get_web_data(airports)
    conditions, stations = ml.get_weather_condition(element_tree.fromstring(content))
    return render_template('projects/metar.html', conditions=conditions, stations=stations, current_page='Projects')


@metar.route('/projects/metar/<string:name>/')
def metar_list(name):
    airports = list(name.split('-'))
    content = ml.get_web_data(airports)
    conditions, stations = ml.get_weather_condition(element_tree.fromstring(content))
    return render_template('projects/metar.html', conditions=conditions, stations=stations, current_page='Projects') 
    

