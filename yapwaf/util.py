"""
Helpful functions for YAPWAF applications
"""

class register(object):

    def __init__(self, method='GET', path='/'):
        self._method = method
        self._path = path

    def __call__(self, f):
        def wrapped(*args):
            f(*args)
        return wrapped
