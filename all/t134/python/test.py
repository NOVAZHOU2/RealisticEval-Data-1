import unittest


class TestIsValidUsername(unittest.TestCase):

    def test_valid_username_with_alphanumeric_characters(self):
        self.assertTrue(is_valid_username('User123'))

    def test_valid_username_with_spaces(self):
        self.assertTrue(is_valid_username('User 123'))

    def test_invalid_username_that_is_too_short(self):
        self.assertFalse(is_valid_username('User'))

    def test_invalid_username_that_is_too_long(self):
        self.assertFalse(is_valid_username('ThisIsAVeryLongUsername'))

    def test_invalid_username_with_special_characters(self):
        self.assertFalse(is_valid_username('User!'))

    def test_invalid_username_with_only_spaces(self):
        self.assertFalse(is_valid_username('     '))

    def test_invalid_input_type_number(self):
        self.assertFalse(is_valid_username(12345))