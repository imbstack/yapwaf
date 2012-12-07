"""
Base file for YAPWAF application
"""
import yapwaf as Y
import conf.env as env
import conf.db as db
import conf.routes as routes

app = Y.App(env, db, routes)
