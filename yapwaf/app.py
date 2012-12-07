"""
Main class of a YAPWAF application.
"""

class App(object):

    def __init__(self, conf, db, routes):
        self.conf = conf
        self.db = db
        self.routes = self.setup_routes(routes)

    def setup_routes(self, routes):
        print routes.routes
        return routes.routes

    def __call__(self, env, start_response):
        print env
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return 'HELLO THERE!\n'
