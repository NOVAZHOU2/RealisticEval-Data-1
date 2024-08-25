import unittest


class TestReplacePhoneNumbers(unittest.TestCase):
    def test_basic_number(self):
        msg = "Call me at 123-456-7890."
        expected = "Call me at [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(msg), expected)

    def test_international_number(self):
        msg = "Contact us at 44 123 456 789."
        expected = "Contact us at [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(msg), expected)

    def test_number_with_parentheses(self):
        msg = "Our office number is 123 456-7890."
        expected = "Our office number is [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(msg), expected)

    def test_number_with_dots(self):
        msg = "Fax us at 123.456.7890."
        expected = "Fax us at [PHONE_NUM]."
        self.assertEqual(replace_phone_numbers(msg), expected)

    def test_no_phone_number(self):
        msg = "Hello, please reply to this email."
        expected = "Hello, please reply to this email."
        self.assertEqual(replace_phone_numbers(msg), expected)

import re


def replace_phone_numbers(text):
    # Define a regex pattern to match phone numbers
    # This pattern matches optional country codes, spaces, dashes, and brackets commonly found in phone numbers
    phone_pattern = r'\b(?:\+\d{1,2}\s?)?(\d{1,4}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,9}[-.\s]?\d{1,9}\b'

    # Replace all matches in the text with [PHONE_NUM]
    replaced_text = re.sub(phone_pattern, '[PHONE_NUM]', text)

    return replaced_text
