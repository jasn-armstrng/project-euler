import unittest
import sum_of_multiples as som

class TestSumOFMultiples(unittest.TestCase):
  def test_sum_of_multiples(self):
    '''Test cases for function sum_of_multiples'''
    result = som.sum_of_multiples(3, 5, 10)
    self.assertEqual(result, 23)

    result = som.sum_of_multiples(3, 5, 100)
    self.assertEqual(result, 2318)

    result = som.sum_of_multiples(3, 5, 1000)
    self.assertEqual(result, 233168)

    result = som.sum_of_multiples(3, 5, 10000)
    self.assertEqual(result, 23331668)

    # Interesting pattern forming from multiples of 3, 5 and powers of 10.

if __name__ == "__main__":
  unittest.main()
