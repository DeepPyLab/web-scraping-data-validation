# tests/test_validator.py

import unittest
from app.validator import validate_data

class TestValidator(unittest.TestCase):

    def test_validate_data_success(self):
        data = {'title': 'Test Page'}
        is_valid, message = validate_data(data)
        self.assertTrue(is_valid)
        self.assertEqual(message, 'Data is valid')

    def test_validate_data_failure_no_title(self):
        data = {}
        is_valid, message = validate_data(data)
        self.assertFalse(is_valid)
        self.assertEqual(message, 'Title is missing or empty')

if __name__ == '__main__':
    unittest.main()
