import unittest
from your_module import format_currency  # Replace with the actual import of your format_currency function

class TestFormatCurrency(unittest.TestCase):
    
    def test_format_currency_usd(self):
        value = 1234.56
        currency_code = 'USD'
        locale = 'en-US'
        expected_output = '\$1,234.56'  # Expected format for USD
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_euro(self):
        value = 1234.56
        currency_code = 'EUR'
        locale = 'en-US'
        expected_output = '€1,234.56'  # Expected format for EUR
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_gbp(self):
        value = 1234.56
        currency_code = 'GBP'
        locale = 'en-GB'
        expected_output = '£1,234.56'  # Expected format for GBP
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_negative(self):
        value = -1234.56
        currency_code = 'USD'
        locale = 'en-US'
        expected_output = '-\$1,234.56'  # Expected format for negative USD
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_zero(self):
        value = 0
        currency_code = 'JPY'
        locale = 'en-JP'
        expected_output = '¥0'  # Expected format for JPY (no decimals)
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)