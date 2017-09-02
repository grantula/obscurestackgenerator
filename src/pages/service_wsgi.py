"""
Package: n/a
Filename: service_wsgi.py
Author(s): Grant W

"""

import os
from pages import application

app = application.create_app()
