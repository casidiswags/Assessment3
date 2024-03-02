import unittest
from app import app  # Replace 'app' with the actual name of your Flask app instance
from database_create import init_db  # Adjust the import statement

class TestGymApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        with app.app_context():
            init_db(app)  # Initialize the database for testing

    def tearDown(self):
        pass  # You may perform cleanup if needed

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Gym App', response.data)

    def test_powerlift_route(self):
        response = self.app.get('/powerlift')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Powerlift Data', response.data)

        # You can add more specific tests related to the content of the powerlift route

    def test_meets_route(self):
        response = self.app.get('/meets')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Meets Data', response.data)

        # You can add more specific tests related to the content of the meets route

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
