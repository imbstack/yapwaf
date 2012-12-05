"""
A simple list of endpoints that will be matched in order.

Each entry is a tuple with
1. A regex to match incoming requests against.  Special notation is used to
   represent arguments.
2. The path for the YAPWAF controller that handles this request.
"""

routes = []

routes.append('<default>', index.Index)
