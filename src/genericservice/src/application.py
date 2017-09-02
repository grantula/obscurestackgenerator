"""
Package: genericservice.src
Filename: application.py
Author(s): Grant W

Main application module.
"""

# Python Imports
import logging
import os

# 3rd Party Imports
from flask import Flask

# Local Imports
from src.v1.routes import genericservice_v1


def create_app():

    app = Flask(__name__)

    setup_config(app)
    configure_logger(app)
    register_status_endpoint(app)

    app.register_blueprint(genericservice_v1)

    return app


def setup_config(app):

    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    app.config['PREFERRED_URL_SCHEME'] = os.environ.get(
            'FLASK_PREFERRED_URL_SCHEME',
            'http'
    )

def configure_logger(app):

    app.route_log = logging.getLogger('genericservice_logger')
    formatter = logging.Formatter('[%(levelname)s] %(funcName)s - line '
            '%(lineno)d: %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    app.route_log.addHandler(handler)
    app.route_log.setLevel(os.environ.get('APP_LOG_LEVEL', 'DEBUG'))

def register_status_endpoint(app):
    @app.route("/status")
    def status():
        return "Service OK", 200
