#!/usr/bin/env python

activate_this = '/var/www/website/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/website')

from run_app import app as application