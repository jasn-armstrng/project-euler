import unittest
import largestPrimeFactor

class TestLargestPrimeFactor(unittest.TestCase):
    def test_largestPrimeFactorOf(self):
        result=largestPrimeFactor.largest_prime_factor_of(8)
        self.assertEqual(result,2)

        result=largestPrimeFactor.largest_prime_factor_of(12)
        self.assertEqual(result,3)

        result=largestPrimeFactor.largest_prime_factor_of(7)
        self.assertEqual(result,7)

        result=largestPrimeFactor.largest_prime_factor_of(17)
        self.assertEqual(result,17)

        result=largestPrimeFactor.largest_prime_factor_of(28)
        self.assertEqual(result,7)

        result=largestPrimeFactor.largest_prime_factor_of(20)
        self.assertEqual(result,5)

        result=largestPrimeFactor.largest_prime_factor_of(600851475143)
        self.assertEqual(result,6857)

    def test_isPrime(self):
        result=largestPrimeFactor.is_prime(1)
        self.assertEqual(result,False)

        result=largestPrimeFactor.is_prime(2)
        self.assertEqual(result,True)

        result=largestPrimeFactor.is_prime(5)
        self.assertEqual(result,True)

        result=largestPrimeFactor.is_prime(6)
        self.assertEqual(result,False)

if __name__=="__main__":
    unittest.main()
