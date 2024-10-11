import os
import unittest
from unittest.mock import patch, mock_open


class TestReadTxtAddJsonBracket(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_valid_json(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [{"key": "value"}])

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    def test_empty_json_array(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [[]])  # Should return an empty list

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}\n')
    def test_valid_json_with_newline(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [{"key": "value"}])


    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_json_with_array(self, mock_file):
        result = read_txt_add_json_bracket("fakefile.txt")
        self.assertEqual(result, [{"key": "value"}])
