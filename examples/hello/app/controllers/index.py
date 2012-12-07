import yapwaf as Y

class Index(Y.Controller):

    @Y.register(method='GET', path='/')  # Default register method
    def hello(self, env):
        return 'index', {'ip': env['REMOTE_ADDR']}

    @Y.register(method='GET', path='/about')  # Will just show a template
    def about(self, env):
        return 'about', None

    @Y.register(method='GET', path='/ping')  # Returns without using a template
    def ping(self, env):
        how_to_text = 'To return text instead of json, just use Y.text'
        return Y.json({'text': how_to_text})

    @Y.register(method='GET', path='/echo/<sid>')  # shows argument use
    def echo(self, env):
        return Y.text(env['sid'])
