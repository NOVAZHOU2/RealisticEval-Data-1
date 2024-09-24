import pandas as pd

def count_value_frequencies(df, column_name):
    """
    Count the frequency of different values in a specified column of a DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to count values.

    Returns:
    pd.Series: A Series with values and their corresponding frequencies.
    """
    return df[column_name].value_counts()
import unittest

import pandas as pd


class TestCountValueFrequencies(unittest.TestCase):

    def test_single_value_column(self):
        df = pd.DataFrame({'A': [1, 1, 1, 1]})
        expected = pd.Series([4], index=[1], name='A')
        result = count_value_frequencies(df, 'A')
        pd.testing.assert_series_equal(result, expected)

    def test_multiple_values(self):
        df = pd.DataFrame({'A': [1, 2, 2, 3, 1]})
        expected = pd.Series([2, 2, 1], index=[1, 2, 3], name='A')
        result = count_value_frequencies(df, 'A')
        pd.testing.assert_series_equal(result, expected)

    def test_empty_column(self):
        df = pd.DataFrame({'A': []})
        expected = pd.Series(dtype=int, name='A')
        result = count_value_frequencies(df, 'A')
        pd.testing.assert_series_equal(result, expected)

    def test_nonexistent_column(self):
        df = pd.DataFrame({'A': [1, 2, 3]})
        with self.assertRaises(KeyError):
            count_value_frequencies(df, 'B')

    def test_string_values(self):
        df = pd.DataFrame({'B': ['apple', 'banana', 'apple', 'orange', 'banana']})
        expected = pd.Series([2, 2, 1], index=['apple', 'banana', 'orange'], name='B')
        result = count_value_frequencies(df, 'B')
        pd.testing.assert_series_equal(result, expected)

if __name__ == '__main__':
    unittest.main()