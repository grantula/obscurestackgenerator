"""
Package: n/a
Filename: service_wsgi.py
Author(s): Grant W

"""
import os
from src import application

app = application.create_app()
