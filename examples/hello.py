"""
This is a simple demo application that handles some of the basic funcionality
of what Yapwaf offers.  Run it with no arguments to try it out!
"""
from yapwaf import YApp, register

app = YApp()

class HelloApp(app.controller):

    @register(method='GET', route='/article')  # Handle GETs to list articles
    def get_article_index(self):
        return 'articles!'

    @register(method='GET', route='/article/<id>')  # Handle GETs to articles
    def get_article(self, _id):
        return 'This is a specific article.'

    @register(method='POST', route='/article/<id>')  # Handle POSTs to articles
    def add_article(self, _id):
        return 'Redirect to the GET of this article!'

    @register()  # Register a handler for the index
    def get_index(self):
        return 'Hello!'


if __name__ == '__main__':
    app.run()

