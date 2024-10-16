import re
import unittest


class TestPhoneNumberDetection(unittest.TestCase):
    def test_with_international_prefix(self):
        self.assertTrue(is_hava_phone_number("+1-800-555-1234"), "Should detect international prefix")

    def test_with_standard_dashes(self):
        self.assertTrue(is_hava_phone_number("800-555-1234"), "Should detect standard format with dashes")

    def test_with_spaces(self):
        self.assertTrue(is_hava_phone_number("800 555 1234"), "Should detect standard format with spaces")

    def test_without_phone_number(self):
        self.assertFalse(is_hava_phone_number("Hello, world!"), "Should not detect any phone number")

    def test_with_text_containing_numbers(self):
        self.assertTrue(is_hava_phone_number("Call me at 800-555-1234 today!"), "Should detect phone number in text")