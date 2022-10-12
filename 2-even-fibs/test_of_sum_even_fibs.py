import unittest
from sum_of_even_fibs import sum_evens

class TestSumOfEvenFibs(unittest.TestCase):

    def test_sum_evens(self):
        '''Test cases for function sum_evens.'''
        result = sum_evens(4000001)
        self.assertEqual(result, 4613732)


if __name__ == "__main__":
    unittest.main()
