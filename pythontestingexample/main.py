import unittest

# __init.py not required here, if you're using Python 3.3 and above
from testing import employee, test_calc


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


if __name__ == "__main__":
    unittest.main()