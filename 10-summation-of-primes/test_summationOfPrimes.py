import unittest
import summationOfPrimes

class TestSummationOfPrimes(unittest.TestCase):
    def test_sumPrimesTo(self):
        result=summationOfPrimes.sumPrimesTo(10)
        self.assertEqual(result,17)

        result=summationOfPrimes.sumPrimesTo(20)
        self.assertEqual(result,77)

        result=summationOfPrimes.sumPrimesTo(2000000)
        self.assertEqual(result,142913828922)

if __name__=="__main__":
    unittest.main()
