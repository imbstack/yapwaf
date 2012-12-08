import yapwaf as Y
from sqlalchemy import Column, Integer, String

class User(Y.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
