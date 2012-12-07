import yapwaf as Y

class Index(Y.Controller):

    @Y.register(method='GET', path='/')
    def hello(self, env):
        return Y.text('testing')
