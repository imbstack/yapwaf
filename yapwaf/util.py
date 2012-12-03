"""
Utility functions and classes for Yapwaf apps.
"""


def register(method='GET', route='/', *args):
    def wrapper(func):
        func._method = method
        func._route = route
        return func
    return wrapper


def call(env, start_resp):
    # for class that is imported, check if it's an app and start it!
