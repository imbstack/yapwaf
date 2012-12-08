"""
The controller base class
"""
from .routes import Route
from .view import View

class Controller(object):

    def __init__(self, entity, env):
        self.entity = entity.strip('/^$')
        if not self.entity:
            self.entity = 'index'
        self.routes = []
        self.register_routes()
        self.env = env

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
            if self.entity == 'index':
                path = '/' + '/'.join(env['PATH_INFO'].split('/')[1:])
            else:
                path = '/' + '/'.join(env['PATH_INFO'].split('/')[2:])
            if route.match(path):
                ans = route.call(env['REQUEST_METHOD'], env['PATH_INFO'], env)
                if ans[1] == 'no_template':
                    return ans[0]
                if '/' in ans[0]:
                    view = View(ans[0].split('/')[0])
                    return view.render(ans[0], ans[1])
                else:
                    view = View(self.entity)
                    return view.render(ans[0], ans[1])
