from tortoise.tests import *

class TestAsyncController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='async', action='index'))
        # Test response...
