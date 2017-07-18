import unittest
from flask_testing import TestCase
from config.AppConfig import app


class TestConfig(TestCase):
    def create_app(self):
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        return app

    def test_one(self):
        assert 2 == 2


if __name__ == '__main__':
    unittest.main()
