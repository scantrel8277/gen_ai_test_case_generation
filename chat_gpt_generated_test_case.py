import unittest

class UserRegistration:
    def register_user(self, username, password, email):
        if not username or not password or not email:
            raise ValueError("All fields are required.")
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long.")
        if '@' not in email:
            raise ValueError("Invalid email address.")
        return {'username': username, 'email': email}

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.registration = UserRegistration()

    def test_successful_registration(self):
        result = self.registration.register_user('testuser', 'password123', 'test@example.com')
        self.assertEqual(result['username'], 'testuser')
        self.assertEqual(result['email'], 'test@example.com')

    def test_missing_username(self):
        with self.assertRaises(ValueError) as context:
            self.registration.register_user('', 'password123', 'test@example.com')
        self.assertEqual(str(context.exception), "All fields are required.")

    def test_short_password(self):
        with self.assertRaises(ValueError) as context:
            self.registration.register_user('testuser', '123', 'test@example.com')
        self.assertEqual(str(context.exception), "Password must be at least 6 characters long.")

    def test_invalid_email(self):
        with self.assertRaises(ValueError) as context:
            self.registration.register_user('testuser', 'password123', 'testexample.com')
        self.assertEqual(str(context.exception), "Invalid email address.")

if __name__ == '__main__':
    unittest.main()
