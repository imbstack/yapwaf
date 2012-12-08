from .app import App
from .controller import Controller
from .routes import Route
from .util import register, text, json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)
session = sessionmaker(bind=engine)()

