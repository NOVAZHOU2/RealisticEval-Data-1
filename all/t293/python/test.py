import unittest

class TestReorderData(unittest.TestCase):
    
    def test_sorts_question_correctly_for_basic_inputs(self):
        scores = [3, 1, 2]
        names = ['Image3', 'Image1', 'Image2']
        ids = [103, 101, 102]
        expected = {
            'resultScores': [1, 2, 3],
            'resultNames': ['Image1', 'Image2', 'Image3'],
            'resultIDs': [101, 102, 103]
        }
        self.assertEqual(reorder_data(scores, names, ids), expected)

    def test_sorts_question_correctly_with_mixed_scores(self):
        scores = [5, 1, 3, 5, 2]
        names = ['Image5', 'Image1', 'Image3', 'Image6', 'Image2']
        ids = [105, 101, 103, 106, 102]
        expected = {
            'resultScores': [1, 2, 3, 5, 5],
            'resultNames': ['Image1', 'Image2', 'Image3', 'Image5', 'Image6'],
            'resultIDs': [101, 102, 103, 105, 106]
        }
        self.assertEqual(reorder_data(scores, names, ids), expected)

    def test_handles_duplicate_scores(self):
        scores = [2, 2, 1]
        names = ['Image2', 'Image3', 'Image1']
        ids = [102, 103, 101]
        expected = {
            'resultScores': [1, 2, 2],
            'resultNames': ['Image1', 'Image2', 'Image3'],
            'resultIDs': [101, 102, 103]
        }
        self.assertEqual(reorder_data(scores, names, ids), expected)

    def test_handles_empty_arrays(self):
        scores = []
        names = []
        ids = []
        expected = {
            'resultScores': [],
            'resultNames': [],
            'resultIDs': []
        }
        self.assertEqual(reorder_data(scores, names, ids), expected)
