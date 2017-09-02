"""
Package: obscurestackgenerator.src.pages.pages.home
Filename: routes.py
Author(s): Grant W

"""

# Python Imports

# 3rd Party Imports
from flask import Blueprint, render_template

# Local Imports


home = Blueprint('home', __name__)


@home.route('/status')
def status():
    return "Service OK", 200


@home.route('/')
def index():
    return render_template('home/index.jinja.html')
