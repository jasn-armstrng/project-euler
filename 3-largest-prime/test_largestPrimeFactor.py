import unittest
import largestPrimeFactor

class TestLargestPrimeFactor(unittest.TestCase):
    def test_largestPrimeFactorOf(self):
        result=largestPrimeFactor.largestPrimeFactorOf(12)
        self.assertEqual(result,3)

        result=largestPrimeFactor.largestPrimeFactorOf(28)
        self.assertEqual(result,7)

        result=largestPrimeFactor.largestPrimeFactorOf(20)
        self.assertEqual(result,5)

        result=largestPrimeFactor.largestPrimeFactorOf(600851475143)
        self.assertEqual(result,6857)

    def test_isPrime(self):
        result=largestPrimeFactor.isPrime(1)
        self.assertEqual(result,False)

        result=largestPrimeFactor.isPrime(2)
        self.assertEqual(result,True)

        result=largestPrimeFactor.isPrime(5)
        self.assertEqual(result,True)

        result=largestPrimeFactor.isPrime(6)
        self.assertEqual(result,False)

if __name__=="__main__":
    unittest.main()
