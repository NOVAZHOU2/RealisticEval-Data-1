class Tester(unittest.TestCase):
    """Test cases for extract_string_from_braces function."""

    def test_basic_extraction(self):
        """Basic extraction."""
        input_data = "This is a sample text with some data {data: \"value\"} and more text."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "{data: \"value\"}")

    def test_no_braces(self):
        """No braces."""
        input_data = "This string has no braces."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "No opening brace found.")

    def test_only_opening_brace(self):
        """Only opening brace."""
        input_data = "This string has an opening brace { but no closing brace."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "No closing brace found.")

    def test_only_closing_brace(self):
        """Only closing brace."""
        input_data = "This string has a closing brace } but no opening brace."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "No opening brace found.")

    def test_multiple_braces(self):
        """Multiple braces."""
        input_data = "First {first} and second {second} braces."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "{first}")

    def test_empty_braces(self):
        """Empty braces."""
        input_data = "This string has empty braces {} and some text."
        result = extract_string_from_braces(input_data)
        self.assertEqual(result, "{}")

