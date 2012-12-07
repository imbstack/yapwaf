"""
Configuring the environment for the YAPWAF app.
Server configuration takes place in conf/wsgi.py
"""
from os import environ

name = 'hello'

# Path for all static assets.  Everything beneath this will be served before
# getting to the YAPWAF app itself.
asset_path = 'public'

if environ.get('Y_PROD'):
    # DO stuff here if production environment is different
    pass

