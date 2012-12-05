"""
Base file for YAPWAF application
"""
import yapwaf as Y
from .conf import env, db

app = Y.app(env, db)
