"""
Main class of a YAPWAF application.
"""

import os
from .util import make_matcher


class App(object):

    def __init__(self, conf, db, routes):
        self.conf = conf
        self.db = db
        self.routes = self.setup_routes(routes)

    def setup_routes(self, routes):
        new_routes = []
        for route in routes.routes:
            new_routes.append(make_matcher(route))
        return new_routes

    def __call__(self, env, start_response):
        if self.conf.level == 'development' and env['PATH_INFO'].startswith('/public'):
            # TODO: set content-size and other nice things
            with open(env['PATH_INFO'].lstrip('/'), 'r') as f:
                if 'css' in env['PATH_INFO']:
                    start_response('200 OK', [('Content-Type', 'text/css')])
                elif 'js' in env['PATH_INFO']:
                    start_response('200 OK', [('Content-Type', 'text/javascript')])
                else:
                    start_response('200 OK', [])
                return f.read()

        for route in self.routes:
            if route[0].match(env['PATH_INFO']):
                resp = route[1](env).route(env)
                if resp:
                    start_response('200 OK', [('Content-Type', 'text')])
                    return resp
        # If we get here, no match was found, so return 404
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return '404 page not found!'
