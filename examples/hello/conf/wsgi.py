"""
gunicorn server configuration
"""
import multiprocessing
from os import environ
import sys

sys.path.insert(0,'hello')

bind = environ.get('BIND','0.0.0.0') + ':' + environ.get('PORT', '8000')
workers = multiprocessing.cpu_count() * 2 + 1
preload = True
