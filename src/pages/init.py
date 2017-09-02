"""
Package: n/a
Filename: init.py
Author(s): Grant W

"""

# Python imports
import os
import subprocess

# Local imports

# 3rd Party Imports

print("Starting init")

process = subprocess.Popen(['envconsul',
                            '-config=/etc/envconsul.hcl',
                            '-consul='+os.environ['CONSUL_ADDRESS'],
                                'uwsgi',
                                '--shared-socket', '0.0.0.0:80',
                                '--http', '=0',
                                '--master',
                                '--cheaper-algo', 'spare',
                                '--cheaper', '2',
                                '--cheaper-initial', '2',
                                '--cheaper-overload', '2',
                                '--cheaper-step', '1',
                                '--workers', '5',
                                '--module', 'service_wsgi:app',
                                '--die-on-term',
                                '--uid', 'sysuser',
                                '--gid', 'sysuser'])

process.wait()
