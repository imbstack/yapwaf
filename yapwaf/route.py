"""
Class to maintain a list of method/route pairs for any
given matched route.
"""

class Route(object):

    def __init__(self, method, matcher, endpoint):
        self.key = matcher
        self.endpoints = {}
        self.endpoints[method] = endpoint

    def call(self, method, *args):
        self.endpoints[method](args)

    def update(self, method, endpoint):
        self.endpoints[method] = endpoint
