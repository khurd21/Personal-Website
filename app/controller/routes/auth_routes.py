from flask import Blueprint, render_template, url_for, request, flash
from werkzeug.utils import redirect
from config import Config
from sqlalchemy import desc

from flask_login import current_user, login_user, logout_user, login_required

from app import session, login
from app.model.admin_model import Admin
from app.model.message_model import Message

auth_routes = Blueprint('auth_routes', __name__)
auth_routes.template_folder = Config.TEMPLATE_FOLDER
auth_routes.static_folder   = Config.STATIC_FOLDER



@login.user_loader
def user_loader(id):
    return session.query(Admin).filter(Admin.id==id).first()


@auth_routes.route('/admin')
@login_required
def admin():
    messages = session.query(Message).order_by(desc(Message.date)).limit(15).all()
    return render_template('admin.html', messages=messages)


@auth_routes.route('/admin/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('auth_routes.admin'))

    if request.method == 'POST':
        user = request.form.get('username')
        pwd  = request.form.get('password')

        if '' in [user, pwd]:
            flash('Please enter all fields.')
        else:
            admin_q = session.query(Admin).filter(Admin.username==user).first()
            if admin_q is not None and admin_q.check_password(pwd):
                login_user(admin_q)
                flash(f'Welcome, {current_user.username}!')
                return redirect(url_for('auth_routes.admin'))
            else:
                flash('Invalid credentials.')

    return render_template('admin_login.html',
                            username=request.form.get('username'),
                            password=request.form.get('password')
                            )


@auth_routes.route('/admin/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_routes.login'))


@auth_routes.route('/admin/delete_message/<id>', methods=['DELETE', 'POST'])
@login_required
def delete_message(id):
    message = session.query(Message).filter(Message.id==id).first()
    if message is None:
        flash('Invalid message.')
        return redirect(url_for('auth_routes.admin'))

    session.delete(message)
    session.commit()

    flash(f'Message from {message.name} deleted.')
    return redirect(url_for('auth_routes.admin'))
