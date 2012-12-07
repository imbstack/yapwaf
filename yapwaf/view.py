"""
Thin wrapper on Jinja2
"""
from jinja2 import Environment, FileSystemLoader
import util as Y


class View(object):

    def __init__(self, entity):
        self.views = Environment(loader=FileSystemLoader(['app/views', 'app/views/%s'%(entity,)]))

    def render(self, view, env):
        template = self.views.get_template(view + '.tmpl')
        env['Y'] = Y
        return template.render(**env)
