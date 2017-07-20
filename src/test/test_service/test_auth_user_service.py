import unittest


class TestAuthUserService(unittest.TestCase):
    def test_index(self):
        from service.AuthUserService import AppUserService
        from main import app
        with app.app_context():
            result = AppUserService.getOneByName("Sazzad")
            self.assertEqual(result["username"], "Sazzad")


if __name__ == '__main__':
    unittest.main()
