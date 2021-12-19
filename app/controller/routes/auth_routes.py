from flask import Blueprint, render_template, url_for, request, flash
from werkzeug.utils import redirect
from config import Config

auth_routes = Blueprint('auth_routes', __name__)
auth_routes.template_folder = Config.TEMPLATE_FOLDER
auth_routes.static_folder   = Config.STATIC_FOLDER

