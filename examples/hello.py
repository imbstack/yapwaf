"""
This is a simple demo application that handles some of the basic funcionality
of what Yapwaf offers.  Run it with no arguments to try it out!
"""
from yapwaf import YApp


class HelloApp(YApp):

    @register(method='GET', route='/article')  # Handle GETs to list articles
    def get_article_index(self):
        return 'articles!'

    @register(method='GET', route='/article/<id>')  # Handle GETs to articles
    def get_article_index(self, _id):
        return 'This is a specific article.'

    @register(YApp.index)  # Register a handler for the index
    def get_article_index(self):
        return 'Hello!'


if __name__ == '__main__':
    app = HelloApp()
    app.run()

