from tortoise.tests import *

class TestTest1Controller(TestController):

    def test_index(self):
        response = self.app.get(url(controller='test1/test1', action='index'))
        # Test response...
