# test_app.py

import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # creates a test client
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home(self):
        # sends HTTP GET request to the application
        # on the specified path
        response = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(response.status_code, 200)

        # assert the response data
        self.assertEqual(response.data, b'<p>Hello, World!</p>')

if __name__ == '__main__':
    unittest.main()

