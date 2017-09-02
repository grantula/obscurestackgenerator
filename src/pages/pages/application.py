"""
Package: obscurestackgenerator.src.page.pages
Filename: application.py
Author(s): Grant W

"""

# Python Imports
import logging
import os

# 3rd Party Imports
from flask import Flask
#
# Local Imports
from pages.home.blueprint import home

def create_app():

    app = Flask('pages', template_folder=".")

    setup_config(app)
    configure_logger(app)
    register_blueprints(app)
    return app


def setup_config(app):

    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    app.config['PREFERRED_URL_SCHEME'] = os.environ.get(
                                            'FLASK_PREFERRED_URL_SCHEME',
                                            'http')
    app.config['TEMPLATES_AUTO_RELOAD'] = os.environ.get(
                                            'FLASK_TEMPLATES_AUTO_RELOAD',
                                            True)


def configure_logger(app):

    app.route_log = logging.getLogger('pages_logger')
    formatter = logging.Formatter('[%(levelname)s] %(funcName)s - '
                                  'line %(lineno)d: %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    app.route_log.addHandler(handler)
    app.route_log.setLevel(os.environ.get('APP_LOG_LEVEL', 'WARN'))


def register_blueprints(app):
    app.register_blueprint(home)
