import unittest
from prime_factors import is_prime, largest_prime_factor

class TestPrimeFactors(unittest.TestCase):

    def test_largest_prime_factor(self):
        '''Test cases for largest_prime_factor function.'''
        result = largest_prime_factor(8)
        self.assertEqual(result,2)

        result = largest_prime_factor(12)
        self.assertEqual(result,3)

        result = largest_prime_factor(7)
        self.assertEqual(result,7)

        result = largest_prime_factor(17)
        self.assertEqual(result,17)

        result = largest_prime_factor(28)
        self.assertEqual(result,7)

        result = largest_prime_factor(20)
        self.assertEqual(result,5)

        result = largest_prime_factor(600851475143)
        self.assertEqual(result,6857)


    def test_is_prime(self):
        '''Test cases for is_prime function.'''
        result = is_prime(1)
        self.assertEqual(result,False)

        result = is_prime(2)
        self.assertEqual(result,True)

        result = is_prime(5)
        self.assertEqual(result,True)

        result = is_prime(6)
        self.assertEqual(result,False)


if __name__ == "__main__":
    unittest.main()
