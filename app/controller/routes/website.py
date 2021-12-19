from config import Config
from flask import Blueprint, render_template, url_for, request, flash, redirect

from app.model.message_model import Message

menu_bar_tabs = Blueprint('menu_bar_tabs', __name__)
menu_bar_tabs.template_folder = Config.TEMPLATE_FOLDER
menu_bar_tabs.static_folder = Config.STATIC_FOLDER

@menu_bar_tabs.route('/')
@menu_bar_tabs.route('/home')
def render_home_page():
    return render_template('home_page.html')


@menu_bar_tabs.route('/resume')
def render_resume_page():
    return render_template('resume.html')


@menu_bar_tabs.route('/contact_me', methods=['GET', 'POST'])
def contact_me():

    if request.method == 'POST':

        message = Message()
        if message.populate(form=request.form):

            message.save_to_db()
            flash(f'Message from {message.name} sent to owner!')
            return redirect(url_for('menu_bar_tabs.render_home_page'))

    f = request.form 
    return render_template('contact_me.html',
                            name=f.get('name'), email=f.get('email'),
                            phone=f.get('phone-number'), message=f.get('message')
                            )


@menu_bar_tabs.route('/about_me')
def about_me():
    return render_template('about_me.html')