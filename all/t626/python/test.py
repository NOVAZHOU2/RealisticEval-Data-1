import os
import unittest


class TestAnswer(unittest.TestCase):
    def setUp(self):
        """Create a temporary file for testing."""
        self.test_file_path = "testFile.txt"
        open(self.test_file_path, 'w').close()  # Create an empty file

    def write_to_file(self, content):
        """Helper method to write to the test file."""
        with open(self.test_file_path, 'w') as writer:
            writer.write(content)

    def test_normal_input(self):
        """Test processing of normal input."""
        self.write_to_file("Line 1\nLine 2 # Comment\nLine 3\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, ["Line 1", "Line 2", "Line 3"])

    def test_only_comments(self):
        """Test processing when only comments are present."""
        self.write_to_file("# This is a comment\n# Another comment\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, [])

    def test_empty_lines(self):
        """Test processing with empty lines."""
        self.write_to_file("Line 1\n\nLine 2\n\n\nLine 3 # Comment\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, ["Line 1", "Line 2", "Line 3"])

    def test_no_inline_comments(self):
        """Test processing when there are no inline comments."""
        self.write_to_file("Line 1\nLine 2\nLine 3\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, ["Line 1", "Line 2", "Line 3"])

    def test_only_new_lines(self):
        """Test processing with only new lines."""
        self.write_to_file("\n\n\n\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, [])

    def test_mixed_content(self):
        """Test processing with mixed content."""
        self.write_to_file("Valid line\n# This is a comment\nLine 2\n# Another comment\n\nLine 3 # End of line comment\n")
        result = read_file_and_process_lines(self.test_file_path)
        self.assertEqual(result, ["Valid line", "Line 2", "Line 3"])

    def tearDown(self):
        """Cleanup after tests."""
        try:
            os.remove(self.test_file_path)
        except OSError:
            pass  # Ignore if the file doesn't exist