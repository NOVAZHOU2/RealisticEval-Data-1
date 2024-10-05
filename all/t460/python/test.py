import unittest


class TestMatrixVectorMultiplication(unittest.TestCase):

    def test_non_square_matrix(self):
        """Test case for a non-square matrix and a compatible vector."""
        matrix = [[1, 2], [3, 4], [5, 6]]
        vector = [2, 3]
        expected_result = [8.0, 18.0, 28.0]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_zero_vector(self):
        """Test case for a matrix and a zero vector."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        vector = [0, 0, 0]
        expected_result = [0.0, 0.0]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_single_element(self):
        """Test case for a single element matrix and vector."""
        matrix = [[5]]
        vector = [3]
        expected_result = [15.0]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected_result)

    def test_single_element_matrix_and_vector(self):
        # Test case with a single element in the matrix and vector
        matrix = [[3]]
        vector = [4]
        expected = [12]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected)

    def test_compatible_sizes(self):
        # Test case with compatible sizes but different dimensions
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        vector = [1, 1, 1]
        expected = [6, 15, 24]
        self.assertEqual(matrix_vector_multiplication(matrix, vector), expected)
