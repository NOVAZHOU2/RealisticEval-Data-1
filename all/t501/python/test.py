import unittest


class TestConvertToShortFormat(unittest.TestCase):

    def test_basic_case(self):
        """ Test a standard input with mixed characters. """
        self.assertEqual(convert_to_short_format("f1_p1_g1_b1_c1"), "fpgbc")

    def test_multiple_segments(self):
        """ Test input with multiple segments. """
        self.assertEqual(convert_to_short_format("a2_b3_c4"), "abc")

    def test_non_alpha_numeric(self):
        """ Test input with non-alphanumeric characters. """
        self.assertEqual(convert_to_short_format("hello_world_test"), "hwt")

    def test_single_segment(self):
        """ Test a single segment input. """
        self.assertEqual(convert_to_short_format("single"), "s")
