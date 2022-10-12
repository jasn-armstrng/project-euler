import unittest
from sum_of_multiples import sum_multiples

class TestSumOFMultiples(unittest.TestCase):

    def test_sum_multiples(self):
        '''Test cases for function sum_of_multiples.'''
        result = sum_multiples(3, 5, 10)
        self.assertEqual(result, 23)

        result = sum_multiples(3, 5, 100)
        self.assertEqual(result, 2318)

        result = sum_multiples(3, 5, 1000)
        self.assertEqual(result, 233168)

        result = sum_multiples(3, 5, 10**4)
        self.assertEqual(result, 23331668)
        # Interesting pattern forming from multiples of 3, 5 and powers of 10.


if __name__ == "__main__":
    unittest.main()
