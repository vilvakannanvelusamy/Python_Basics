import unittest
from count_nine_divisors.main import count_numbers_with_nine_divisors

class TestCountNineDivisors(unittest.TestCase):

    def test_count_nine_divisors(self):
        self.assertEqual(count_numbers_with_nine_divisors(100), 2)
        self.assertEqual(count_numbers_with_nine_divisors(200), 3)
        self.assertEqual(count_numbers_with_nine_divisors(36), 1)
        self.assertEqual(count_numbers_with_nine_divisors(1), 0)
        self.assertEqual(count_numbers_with_nine_divisors(1000), 4)

if __name__ == '__main__':
    unittest.main()