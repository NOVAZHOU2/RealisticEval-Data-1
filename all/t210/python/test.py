class TestFibonacci(Tester):
    def test_fibonacci_0(self):
        """Test Case 1: Fibonacci of 0 should be 0"""
        self.assertEqual(self.fibonacci_recursive(0), 0)

    def test_fibonacci_1(self):
        """Test Case 2: Fibonacci of 1 should be 1"""
        self.assertEqual(self.fibonacci_recursive(1), 1)

    def test_fibonacci_5(self):
        """Test Case 3: Fibonacci of 5 should be 5"""
        self.assertEqual(self.fibonacci_recursive(5), 5)

    def test_fibonacci_10(self):
        """Test Case 4: Fibonacci of 10 should be 55"""
        self.assertEqual(self.fibonacci_recursive(10), 55)

    def test_fibonacci_20(self):
        """Test Case 5: Fibonacci of 20 should be 6765"""
        self.assertEqual(self.fibonacci_recursive(20), 6765)
