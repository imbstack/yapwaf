"""
Main class of a Yapwaf application.
"""
from .route import Route


class App(object):

    def __init__(self):
        self.routes = []
        self.register_routes()
        print self.routes

    def register_routes(self):
        for funcname in dir(self):
            func = getattr(self, funcname)
            if hasattr(func, '_route') and hasattr(func, '_method'):
                self.update_routes(func._method, func._route, func)

    def update_routes(self, method, matcher, endpoint):
        for route in self.routes:
            if route.key == matcher:
                route.update(method, endpoint)
                return
        # If the route has not been added to the routes yet
        self.routes.append(Route(method, matcher, endpoint))
