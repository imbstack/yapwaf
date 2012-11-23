import Testify as T
from factories import mock_db_factory, mock_server_factory, mock_template_factory


class ApplicationTest(T.TestCase):

    @T.class_setup
    def setup_mocks(self):
        self.db = mock_db_factory.make()
        self.server = mock_server_factory.make()
        self.template = mock_template_factory.make()
