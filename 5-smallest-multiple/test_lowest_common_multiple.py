import unittest
from lowest_common_multiple import gcd, lcm

class TestLowestComonMultiple(unittest.TestCase):

    def test_gcd(self):
        '''Test cases for the gcd function.'''
        result = gcd([48, 18])
        self.assertEqual(result, 6)

        result = gcd([18, 48])
        self.assertEqual(result, 6)

        result = gcd([1, 2])
        self.assertEqual(result, 1)

        result = gcd([14, 35])
        self.assertEqual(result, 7)

        result = gcd([22, 66])
        self.assertEqual(result, 22)


    def test_lcm(self):
        '''Test cases for the lcm function.'''
        result = lcm([0, 1])
        self.assertEqual(result, 0)

        result = lcm([0, 1, 2])
        self.assertEqual(result, 0)

        result = lcm([1, 1])
        self.assertEqual(result, 1)

        result = lcm([1, 1, 2])
        self.assertEqual(result, 2)

        result = lcm([i for i in range(1, 9)])
        self.assertEqual(result, 840)

        result = lcm([i for i in range(1, 5)])
        self.assertEqual(result, 12)

        result = lcm([i for i in range(1, 7)])
        self.assertEqual(result, 60)

        result = lcm([i for i in range(1, 21)])
        self.assertEqual(result, 232792560)


if __name__ == "__main__":
    unittest.main()
