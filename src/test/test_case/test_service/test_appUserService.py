import unittest
from test.test_config.TestConfig import TestConfig


class TestAppUserService(TestConfig):
    def test_getAll(self):
        assert 3 == 3


if __name__ == '__main__':
    unittest.main()
