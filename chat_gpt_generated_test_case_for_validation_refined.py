import unittest

class UserRegistration:
    def register_user(self, username, password, email):
        # Validate that username, password, and email are provided
        if not username or not password or not email:
            raise ValueError("All fields are required.")
        # Validate password length
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long.")
        # Validate email format
        if '@' not in email:
            raise ValueError("Invalid email address.")
        return {'username': username, 'email': email}

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.registration = UserRegistration()

    def test_successful_registration(self):
        result = self.registration.register_user('validUser', 'validPass123', 'user@example.com')
        self.assertEqual(result['username'], 'validUser')
        self.assertEqual(result['email'], 'user@example.com')

    def test_missing_username(self):
        with self.assertRaises(ValueError) as context:
            self.registration.register_user('', 'validPass123', 'user@example.com')
        self.assertEqual(str(context.exception), "All fields are required.")

    def test_missing_password(self):
        with self.assertRaises(ValueError) as context:
            self.registration.register_user('validUser', '', 'user@example.com')
        self.assertEqual(str(context.exception), "All fields are required.")

    def test_missing_email(self):
        with self.assertRaises(ValueError) as context:
            self.registration.register_user('validUser', 'validPass123', '')
        self.assertEqual(str(context.exception), "All fields are required.")

    def test_short_password(self):
        with self.assertRaises(ValueError) as context:
            self.registration.register_user('validUser', '123', 'user@example.com')
        self.assertEqual(str(context.exception), "Password must be at least 6 characters long.")

    def test_invalid_email_format(self):
        with self.assertRaises(ValueError) as context:
            self.registration.register_user('validUser', 'validPass123', 'userexample.com')
        self.assertEqual(str(context.exception), "Invalid email address.")

    def test_email_without_at_symbol(self):
        with self.assertRaises(ValueError) as context:
            self.registration.register_user('validUser', 'validPass123', 'userexample.com')
        self.assertEqual(str(context.exception), "Invalid email address.")

    def test_email_with_multiple_at_symbols(self):
        with self.assertRaises(ValueError) as context:
            self.registration.register_user('validUser', 'validPass123', 'user@@example.com')
        self.assertEqual(str(context.exception), "Invalid email address.")

if __name__ == '__main__':
    unittest.main()
