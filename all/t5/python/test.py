import unittest


class TestMatrixMultiplication(unittest.TestCase):
    def test_standard_matrices(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected, "Should correctly multiply standard matrices")

    def test_identity_matrix(self):
        mat1 = [[1, 0], [0, 1]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[5, 6], [7, 8]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "Multiplying by the identity matrix should yield the answer.py matrix")

    def test_zero_matrix(self):
        mat1 = [[0, 0], [0, 0]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[0, 0], [0, 0]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "Multiplying by the zero matrix should yield a zero matrix")

    def test_square_matrix_multiplication(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "The multiplication of two square matrices should yield the correct product")

    def test_large_identity_matrix(self):
        mat1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        mat2 = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
        expected = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
        self.assertEqual(matrix_multiply(mat1, mat2), expected,
                         "Multiplying by the larger identity matrix should yield the answer matrix")
