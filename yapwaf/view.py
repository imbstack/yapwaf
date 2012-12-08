"""
Thin wrapper on Jinja2
"""
from jinja2 import Environment, FileSystemLoader
import util as Y


class View(object):

    def __init__(self, entity):
        """Instantiate the view with the proper directory to look in for templates"""
        self.views = Environment(loader=FileSystemLoader(['app/views', 'app/views/%s'%(entity,)]))

    def render(self, view, env):
        """Get the template and render it with the standard environment in
        to YAPWAF to provide the utility helper functions.
        """
        template = self.views.get_template(view + '.tmpl')
        env['Y'] = Y
        return template.render(**env)
