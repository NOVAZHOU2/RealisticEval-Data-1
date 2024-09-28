import unittest

import numpy as np


class TestScalePointCloud(unittest.TestCase):

    def test_simple_scaling(self):
        """Test scaling of a single point."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        scale_factor = 2.0
        expected_output = np.array([[2.0, 4.0, 6.0]])
        np.testing.assert_array_almost_equal(scale_point_cloud(point_cloud, scale_factor), expected_output)

    def test_multiple_points_scaling(self):
        """Test scaling of multiple points."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        scale_factor = 0.5
        expected_output = np.array([[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]])
        np.testing.assert_array_almost_equal(scale_point_cloud(point_cloud, scale_factor), expected_output)

    def test_zero_scaling(self):
        """Test scaling by a factor of zero (should return a point cloud of zeros)."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        scale_factor = 0.0
        expected_output = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        np.testing.assert_array_almost_equal(scale_point_cloud(point_cloud, scale_factor), expected_output)

    def test_negative_scaling(self):
        """Test scaling with a negative factor."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        scale_factor = -2.0
        expected_output = np.array([[-2.0, -4.0, -6.0]])
        np.testing.assert_array_almost_equal(scale_point_cloud(point_cloud, scale_factor), expected_output)

    def test_invalid_point_cloud_shape(self):
        """Test handling of an invalid point cloud shape."""
        point_cloud = np.array([[1.0, 2.0]])  # Invalid shape, should raise an error
        scale_factor = 2.0
        with self.assertRaises(ValueError) as context:
            scale_point_cloud(point_cloud, scale_factor)
        self.assertEqual(str(context.exception), "point_cloud must be a 2D array with shape (N, 3)")