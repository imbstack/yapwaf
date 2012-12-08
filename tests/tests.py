import testify as T
import yapwaf as Y
import test_env as conf
import test_db as db
import test_routes as routes


class ApplicationTest(T.TestCase):

    @T.class_setup
    def setup_mocks(self):
        self.app = Y.App(conf, db, routes)

    def test_routes(self):
        routelist = self.app.setup_routes(routes)
        T.assert_equal(routelist[0][0].pattern, '^/')

    def test_add_route(self):
        def temp():
            return
        routes.routes.append(('/test', temp))
        routelist = self.app.setup_routes(routes)
        T.assert_equal(routelist[1][0].pattern, '^/test')

    def test_call(self):
        env = {'PATH_INFO': '/', 'REQUEST_METHOD': 'GET'}
        def start_response(status, headers):
            T.assert_equal('200 OK', status)
        res = self.app(env, start_response)
        T.assert_equal(['testing'], res)


class ControllerTest(T.TestCase):

    @T.class_setup
    def setup_mocks(self):
        self.env = {'PATH_INFO': '/', 'REQUEST_METHOD': 'GET'}
        self.controller = Y.Controller('/', self.env)
        def temp(arg):
            return Y.text('testing')
        self.controller.routes.append(Y.Route('GET', '/', temp))

    def test_update_routes(self):
        def temp(arg):
            return Y.text('testing')
        self.controller.update_routes('POST', '/test', temp)
        T.assert_equal(self.controller.routes[1].matcher.pattern, '^/test$')

    def test_route(self):
        T.assert_equal(self.controller.route(self.env), ['testing'])


class UtilTest(T.TestCase):

    def test_test(self):
        T.assert_equal(Y.util.text('testing'), (['testing'], 'no_template'))

    def test_json(self):
        T.assert_equal(Y.util.json('[testing]'), (['"[testing]"'], 'no_template'))

    def test_css(self):
        T.assert_equal(Y.util.css('a'), '<link rel="stylesheet" type="text/css" href="/public/css/a.css">')

    def test_js(self):
        T.assert_equal(Y.util.css('a'), '<link rel="stylesheet" type="text/css" href="/public/css/a.css">')

    def test_matcher(self):
        match = Y.util.make_matcher(('/test', 'temp'))
        T.assert_equal(match[0].pattern, '^/test')

    def test_end_matcher(self):
        match = Y.util.make_end_matcher('/test/<param>')
        T.assert_equal(match[0].pattern, '^/test/[a-zA-Z0-9]+$')
        T.assert_equal(match[1], 'param')
