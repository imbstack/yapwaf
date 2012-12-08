import yapwaf as Y
from app.models.user import User as U

class User(Y.Controller):

    @Y.register(method='GET', path='/')  # Show all users
    def index(self, env):
        return 'index', {}

    @Y.register(method='GET', path='/<uid>')  # Just show a user
    def user(self, env):
        user = Y.session.query(U).filter(U.id == 1).first()
        return 'single', {'user': user}
