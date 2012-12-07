"""
The controller base class
"""
from .routes import Route
from .view import View

class Controller(object):

    def __init__(self, env):
        self.routes = []
        self.register_routes()
        self.env = self.transform_env(env)

    def register_routes(self):
        for funcname in dir(self):
            func = getattr(self, funcname)
            if hasattr(func, '_method') and hasattr(func, '_path'):
                self.update_routes(func._method, func._path, func)

    def update_routes(self, method, matcher, endpoint):
        for route in self.routes:
            if route.key == matcher:
                route.update(method, endpoint)
                return
        # If the route has not been added to the routes yet
        self.routes.append(Route(method, matcher, endpoint))

    def route(self, env):
        for route in self.routes:
            if route.match(env['PATH_INFO']):
                ans = route.call(env['REQUEST_METHOD'], env['PATH_INFO'], env)
                if ans[1] == 'no_template':
                    return ans[0]
                if '/' in ans[0]:
                    print 'HANDLE PATH STUFF LATER'
                else:
                    view = View(env['handler'])
                    return view.render(ans[0], ans[1])

    def transform_env(self, env):
        # TODO: make the keys in the dict nicer!
        return env
