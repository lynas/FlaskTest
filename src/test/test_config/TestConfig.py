import unittest
from main import app
from flask import json


class TestConfig(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')
        rr = json.loads(response.data)
        self.assertEqual(rr["success"], True)


if __name__ == '__main__':
    unittest.main()
