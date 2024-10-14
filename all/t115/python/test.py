import unittest


class TestSortByKey(unittest.TestCase):

    def test_empty_array(self):
        result = sort_by_key([], 'name')
        self.assertEqual(result, [])

    def test_single_element(self):
        single_element_array = [{'name': 'Apple'}]
        self.assertEqual(sort_by_key(single_element_array, 'name'), [{'name': 'Apple'}])

    def test_sort_by_key(self):
        test_data = [
            {'name': 'banana'},
            {'name': 'apple'},
            {'name': 'orange'}
        ]
        expected = [
            {'name': 'apple'},
            {'name': 'banana'},
            {'name': 'orange'}
        ]
        self.assertEqual(sort_by_key(test_data, 'name'), expected)

    def test_case_insensitive_sorting(self):
        mixed_case_array = [
            {'name': 'banana'},
            {'name': 'Apple'},
            {'name': 'orange'}
        ]
        expected = [
            {'name': 'Apple'},
            {'name': 'banana'},
            {'name': 'orange'}
        ]
        self.assertEqual(sort_by_key(mixed_case_array, 'name'), expected)
