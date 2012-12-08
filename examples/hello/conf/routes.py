"""
A simple list of endpoints that will be matched in order.

Each entry is a tuple with
1. A regex to match incoming requests against.  Special notation is used to
   represent arguments.
2. The path for the YAPWAF controller that handles this request.
"""
import app.controllers.index as index
import app.controllers.user as user

routes = []

routes.append(('/user', user.User))
routes.append(('/', index.Index))
