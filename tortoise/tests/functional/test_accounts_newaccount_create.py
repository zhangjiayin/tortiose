from tortoise.tests import *

class TestCreateController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='accounts/newaccount/create', action='index'))
        # Test response...
