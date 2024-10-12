import unittest

class TestCalculateRemainingPayment(unittest.TestCase):
    
    def test_typical_loan_conditions(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 24), 0, places=2)

    def test_high_interest_rate(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.1, 12), 0, places=2)

    def test_low_interest_rate(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.001, 60), 0, places=2)

    def test_very_short_term(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 1), 0, places=2)

    def test_no_payments(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 0), 10000, places=2)

    def test_long_term(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 360), 0, places=2)