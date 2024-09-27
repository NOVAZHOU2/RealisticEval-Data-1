def write_unique_line_to_file(filename: str, line_content: str):
    """
    Writes a line to a text file only if the line with the same content does not already exist.

    Args:
        filename (str): The name of the file to write to.
        line_content (str): The content of the line to write.

    Returns:
        None
    """
    # Check if the line_content already exists in the file
    with open(filename, 'r') as file:
        if line_content in file.read():
            print(f"Line '{line_content}' already exists in '{filename}'. Not writing again.")
            return

    # If line_content is not found, append it to the file
    with open(filename, 'a') as file:
        file.write(line_content + '\n')
        print(f"Line '{line_content}' successfully written to '{filename}'.")
import unittest
import os


class TestWriteUniqueLineToFile(unittest.TestCase):
    def setUp(self):
        # Setup: create a temporary file for testing.
        self.filename = 'test_file.txt'
        with open(self.filename, 'w') as file:
            file.write('')

    def test_write_new_line(self):
        # Test case 1: Writing a new line to an empty file.
        line_content = "First unique line."
        write_unique_line_to_file(self.filename, line_content)
        with open(self.filename, 'r') as file:
            self.assertIn(line_content, file.read())

    def test_write_duplicate_line(self):
        # Test case 2: Attempting to write a duplicate line.
        line_content = "First unique line."
        # Write the line once.
        write_unique_line_to_file(self.filename, line_content)
        # Attempt to write it again.
        write_unique_line_to_file(self.filename, line_content)
        # Check if the line was written only once.
        with open(self.filename, 'r') as file:
            self.assertEqual(file.read().strip().count(line_content), 1)

    def test_write_multiple_unique_lines(self):
        # Test case 3: Writing multiple unique lines.
        lines = ["First unique line.", "Second unique line.", "Third unique line."]
        for line in lines:
            write_unique_line_to_file(self.filename, line)
        with open(self.filename, 'r') as file:
            file_content = file.read()
            for line in lines:
                self.assertIn(line, file_content)

    def test_write_empty_line(self):
        # Test case 5: Writing an empty line, should not write.
        line_content = ""
        write_unique_line_to_file(self.filename, line_content)
        with open(self.filename, 'r') as file:
            self.assertEqual(file.read(), "")

if __name__ == '__main__':
    unittest.main()