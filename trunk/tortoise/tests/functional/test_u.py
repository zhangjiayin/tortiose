from tortoise.tests import *

class TestUController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='u', action='index'))
        # Test response...
