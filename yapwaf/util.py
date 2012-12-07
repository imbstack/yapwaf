"""
Helpful functions for YAPWAF applications
"""
import json as J
import re as RE

name_match = '<[a-zA-Z0-9]+>'


class register(object):

    def __init__(self, method='GET', path='/'):
        self._method = method
        self._path = path

    def __call__(self, f):
        def wrapped(*args):
            args[1]['handler'] = 'index'  # for choosing the view
            return f(*args)
        wrapped._method = self._method
        wrapped._path = self._path
        return wrapped


def text(t):
    return [t], 'no_template'


def json(t):
    return [J.dumps(t)], 'no_template'


def js(f):
    return '<script type="text/javascript" src="/public/js%s.js"></script>'%(f,)


def css(f):
    return '<link rel="stylesheet" type="text/css" href="/public/css/%s.css">'%(f,)

def link(name, href):
    return '<a href="%s">%s</a>'%(href, name)


def make_matcher(route):
    """Simply take the path and turn into a regular expression to match
    against incoming paths.  This is for the top level routing and therefore
    does not need to handle arguments, etc.
    """
    return RE.compile('^'+route[0]), route[1]


def make_end_matcher(path):
    """Given a path to match against incoming requests,
    take any text between '<' and '>' characters and turn it
    into arguments to be passed to the endpoint
    """
    try:
        name = RE.search(name_match, path).group(0).strip('><')
    except AttributeError:
        name = ''
    new_match = RE.sub('/'+name_match, '/'+name_match.strip('><'), path)
    return RE.compile('^'+new_match+'$'), name
