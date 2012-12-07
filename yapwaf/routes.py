"""
Functions to handle route update tasks.
"""

from .util import make_matcher, make_end_matcher


class Route(object):

    def __init__(self, method, matcher, endpoint):
        self.key = matcher
        self.matcher, self.argname = make_end_matcher(matcher)
        self.endpoints = {}
        self.endpoints[method] = endpoint

    def match(self, path):
        return self.matcher.match(path)

    def call(self, method, path, env):
        print '%s: %s' % (method, path)
        # TODO: perhaps use regex again if multiple args are expected?
        args = {self.argname: path.split('/')[-1]}
        env.update(args)
        return self.endpoints[method](env)

    def update(self, method, endpoint):
        self.endpoints[method] = endpoint
