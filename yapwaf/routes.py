"""
Functions to handle route update tasks.
"""

from .util import make_matcher, make_end_matcher


class Route(object):

    def __init__(self, method, matcher, endpoint):
        """Instantiate the Route object with the first endpoint"""
        self.key = matcher
        self.matcher, self.argname = make_end_matcher(matcher)
        self.endpoints = {}
        self.endpoints[method] = endpoint

    def match(self, path):
        """Simply call the regex match on the supplied path"""
        return self.matcher.match(path)

    def call(self, method, path, env):
        """Call the endpoint that is being routed to"""
        print '%s: %s' % (method, path)
        args = {self.argname: path.split('/')[-1]}
        env.update(args)
        return self.endpoints[method](env)

    def update(self, method, endpoint):
        """Add a new HTTP method to the path route"""
        self.endpoints[method] = endpoint
