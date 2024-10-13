import unittest

class Tester(unittest.TestCase):
    """Unit tests for the Shell sort functionality."""

    def test_already_sorted_array(self):
        """Test Case 1: Already sorted array."""
        arr = [1, 2, 3, 4, 5]
        shell_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_reverse_sorted_array(self):
        """Test Case 2: Reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        shell_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_array_with_duplicate_elements(self):
        """Test Case 3: Array with duplicate elements."""
        arr = [4, 2, 2, 4, 1]
        shell_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_array_with_negative_numbers(self):
        """Test Case 4: Array with negative numbers."""
        arr = [-3, -1, -4, -2, 0]
        shell_sort(arr)
        self.assertTrue(is_sorted(arr))

    def test_empty_array(self):
        """Test Case 5: Empty array."""
        arr = []
        shell_sort(arr)
        self.assertTrue(is_sorted(arr))
