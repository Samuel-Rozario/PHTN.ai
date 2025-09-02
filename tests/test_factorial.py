import unittest
from mini_package import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_negative(self):
        import pytest
        try:
            factorial(-1)
        except ValueError:
            pass
        else:
            raise AssertionError("Negative input did not raise ValueError")

if __name__ == "__main__":
    unittest.main()
