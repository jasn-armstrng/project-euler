import unittest
import summationOfPrimes

class TestSummationOfPrimes(unittest.TestCase):
    def test_sumPrimesTo(self):
        result=summationOfPrimes.sumPrimesTo(10)
        self.assertEqual(result,17)

if __name__=="__main__":
    unittest.main()
