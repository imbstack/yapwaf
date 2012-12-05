"""
gunicorn server configuration
"""
import multiprocessing
from os import environ

bind = '127.0.0.1:' + environ.get('PORT', '8000')
workers = multiprocessing.cpu_count() * 2 + 1
preload = True
