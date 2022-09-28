import unittest
import thousandAndFirstPrime

class TestThousandAndFirstPrime(unittest.TestCase):
    # Testing isPrime function
    def test_isPrime(self):
        print("Testing the isPrime function")
        result=thousandAndFirstPrime.isPrime(1)
        self.assertEqual(result, False)

        result=thousandAndFirstPrime.isPrime(2)
        self.assertEqual(result, True)

        result=thousandAndFirstPrime.isPrime(61)
        self.assertEqual(result, True)

    # Testing nthPrime function
    def test_nthPrime(self):
        print("Testing the nthPrime function")
        result=thousandAndFirstPrime.nthPrime(6)
        self.assertEqual(result, 13)

        result=thousandAndFirstPrime.nthPrime(100)
        self.assertEqual(result, 541)

        result=thousandAndFirstPrime.nthPrime(10001)
        self.assertEqual(result, 104743)

if __name__=="__main__":
    unittest.main()
