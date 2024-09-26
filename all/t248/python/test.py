import unittest


class TestSanitizeData(unittest.TestCase):
    def test_empty_dict(self):
        """ Test with an empty dictionary. """
        data = {}
        key_to_remove = ["email", "metadata"]

        expected = {}
        self.assertEqual(sanitize_data(data, key_to_remove), expected)

    def test_remove_default_keys(self):
        """ Test removing default keys from a nested structure. """
        data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "metadata": {"submitted_at": "2021-07-10", "status": "pending"},
            "comments": ["Good", "Needs review"]
        }
        key_to_remove = ["email", "metadata"]
        expected = {
            "name": "John Doe",
            "comments": ["Good", "Needs review"]
        }
        self.assertEqual(sanitize_data(data, key_to_remove), expected)

    def test_specified_key_to_remove(self):
        """ Test removing a specified key from the dictionary. """
        data = {
            "name": "John Doe",
            "location": "Earth",
            "email": "johndoe@example.com"
        }
        expected = {
            "name": "John Doe",
            "location": "Earth"
        }
        self.assertEqual(sanitize_data(data, key_to_remove=["email"]), expected)

    def test_list_of_dicts(self):
        """ Test a list containing dictionaries. """
        data = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"}
        ]
        key_to_remove = ["email", "metadata"]
        expected = [
            {"name": "Alice"},
            {"name": "Bob"}
        ]
        self.assertEqual(sanitize_data(data,key_to_remove), expected)

    def test_non_dict_non_list(self):
        """ Test with non-dict and non-list question types. """
        data = "Hello, world!"
        expected = "Hello, world!"
        self.assertEqual(sanitize_data(data), expected)
