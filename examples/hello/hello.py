"""
Base file for YAPWAF application
"""
import yapwaf as Y
import conf.env as env
import conf.db as db
import conf.routes as routes

# For testing purposes, add a user to the database
from app.models.user import User
Y.Base.metadata.create_all(Y.engine)
user = User('Brian', 'Stack')
Y.session.add(user)
Y.session.commit()

app = Y.App(env, db, routes)
