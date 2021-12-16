from app.model.menu_bar_state import MENU_BAR_STATE
from flask import Blueprint, render_template, get_template_attribute, url_for
import ast

menu_bar_tabs = Blueprint('menu_bar_tabs', __name__)


@menu_bar_tabs.route('/')
def render_home_page():
    #hello = get_template_attribute('base.html', 'hello')
    #return hello('World!')
    return render_template('home_page.html')


@menu_bar_tabs.route('/projects')
def render_projects_page():
    return render_template(
            'projects_page.html',
            current_page = MENU_BAR_STATE.PROJECTS,
            MENU_BAR_STATE = MENU_BAR_STATE
            )


@menu_bar_tabs.route('/my_music')
def render_my_music_page():
    return render_template(
            'my_music_page.html',
            current_page = MENU_BAR_STATE.MY_MUSIC,
            MENU_BAR_STATE = MENU_BAR_STATE
            )


@menu_bar_tabs.route('/about_me')
def render_about_me_page():
    return render_template(
            'about_me_page.html',
            current_page = MENU_BAR_STATE.ABOUT_ME,
            MENU_BAR_STATE = MENU_BAR_STATE
            )


@menu_bar_tabs.route('/my_music/tabs')
def render_my_tabs_page():
    with menu_bar_tabs.open_resource('../static/music_tabs/songs.txt', 'r') as f_:
        content = f_.read()
        playlist = ast.literal_eval(content)
    return render_template(
            'my_music_tabs_page.html',
            playlist = playlist,
            current_page = MENU_BAR_STATE.MY_MUSIC,
            MENU_BAR_STATE = MENU_BAR_STATE,
            )

@menu_bar_tabs.route('/resume')
def render_resume_page():
    return render_template('resume.html')
