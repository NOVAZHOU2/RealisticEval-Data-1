import unittest


class TestRenameFilePath(unittest.TestCase):
    def test_rename_with_colon_in_filename(self):
        # Test path with colon in the filename
        path = 'C:\\Users\\example\\Documents\\report:2023.txt'
        expected = 'C:\\Users\\example\\Documents\\report_2023.txt'
        self.assertEqual(rename_file_path(path), expected)

    def test_rename_without_colon_in_filename(self):
        # Test path without colon in the filename
        path = 'C:\\Users\\example\\Documents\\report2023.txt'
        expected = 'C:\\Users\\example\\Documents\\report2023.txt'
        self.assertEqual(rename_file_path(path), expected)

    def test_rename_with_multiple_colons_in_filename(self):
        # Test path with multiple colons in the filename
        path = 'C:\\Users\\example\\Documents\\project:report:2023.txt'
        expected = 'C:\\Users\\example\\Documents\\project_report_2023.txt'
        self.assertEqual(rename_file_path(path), expected)

    def test_rename_with_colon_at_end_of_filename(self):
        # Test path with a colon at the end of the filename
        path = 'C:\\Users\\example\\Documents\\backup:'
        expected = 'C:\\Users\\example\\Documents\\backup_'
        self.assertEqual(rename_file_path(path), expected)

    def test_rename_with_colon_at_start_of_filename(self):
        # Test path with a colon at the start of the filename
        path = 'C:\\Users\\example\\Documents\\:initial_setup.txt'
        expected = 'C:\\Users\\example\\Documents\\_initial_setup.txt'
        self.assertEqual(rename_file_path(path), expected)
