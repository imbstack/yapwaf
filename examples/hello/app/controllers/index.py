import yapwaf as Y

class Index(Y.controller):

    @Y.register()  # Default register method
    def hello(self):
        return 'index', {'ip': req.ip}

    @Y.register(method='GET', path='/about')  # Will just show a template
    def about(self):
        return 'about'

    @Y.register(method='GET', path='/ping')  # Returns without using a template
    def ping(self):
        how_to_text = 'To return text instead of json, just use Y.text'
        return Y.json({'text': how_to_text})
