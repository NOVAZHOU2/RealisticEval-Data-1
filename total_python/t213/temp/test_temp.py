import unittest

import numpy as np


class TestIm2Col(unittest.TestCase):

    def test_single_channel_no_padding_stride_1(self):
        image = np.array([
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
        ])  # Shape (1, 4, 4)
        filter_height = 2
        filter_width = 2
        stride = 1
        padding = 0

        expected_output = np.array([
            [1, 2, 3, 5, 6, 7, 9, 10, 11],
            [2, 3, 4, 6, 7, 8, 10, 11, 12],
            [5, 6, 7, 9, 10, 11, 13, 14, 15],
            [6, 7, 8, 10, 11, 12, 14, 15, 16]
        ])
        output = im2col(image, filter_height, filter_width, stride, padding)
        np.testing.assert_array_equal(output, expected_output)

    def test_single_channel_no_padding_stride_2(self):
        image = np.array([
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
        ])  # Shape (1, 4, 4)
        filter_height = 2
        filter_width = 2
        stride = 2
        padding = 0

        expected_output = np.array([
            [1, 3, 9, 11],
            [2, 4, 10, 12],
            [5, 7, 13, 15],
            [6, 8, 14, 16]
        ])
        output = im2col(image, filter_height, filter_width, stride, padding)
        np.testing.assert_array_equal(output, expected_output)

    def test_multi_channel_no_padding_stride_1(self):
        image = np.array([
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [[9, 8, 7],
             [6, 5, 4],
             [3, 2, 1]]
        ])  # Shape (2, 3, 3), 2 channels
        filter_height = 2
        filter_width = 2
        stride = 1
        padding = 0

        expected_output = np.array([
            [1, 2, 4, 5],
            [2, 3, 5, 6],
            [4, 5, 7, 8],
            [5, 6, 8, 9],
            [9, 8, 6, 5],
            [8, 7, 5, 4],
            [6, 5, 3, 2],
            [5, 4, 2, 1]
        ])
        output = im2col(image, filter_height, filter_width, stride, padding)
        np.testing.assert_array_equal(output, expected_output)

import unittest
import numpy as np

def im2col(image, filter_height, filter_width, stride=1, padding=0):
    """
    Apply the im2col operation to an input image.

    Parameters:
    - image (numpy array): The input image of shape (C, H, W) where:
        C: Number of channels
        H: Height of the image
        W: Width of the image
    - filter_height (int): Height of the filter
    - filter_width (int): Width of the filter
    - stride (int): Stride of the filter
    - padding (int): Number of pixels to pad the input image

    Returns:
    - col (numpy array): A 2D array where each column is a flattened filter region
    """
    C, H, W = image.shape
    out_height = (H + 2 * padding - filter_height) // stride + 1
    out_width = (W + 2 * padding - filter_width) // stride + 1

    # Apply padding to the image
    padded_image = np.pad(image, ((0, 0), (padding, padding), (padding, padding)), mode='constant')

    # Initialize the column matrix
    col = np.zeros((C * filter_height * filter_width, out_height * out_width))

    # Fill the column matrix
    col_idx = 0
    for y in range(0, H + 2 * padding - filter_height + 1, stride):
        for x in range(0, W + 2 * padding - filter_width + 1, stride):
            patch = padded_image[:, y:y + filter_height, x:x + filter_width]
            col[:, col_idx] = patch.flatten()
            col_idx += 1

    return col