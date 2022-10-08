import unittest
import specialPythagoreanTriple

class TestSpecialPythagoreanTriple(unittest.TestCase):
    def test_pythagoreanTripleWithSum(self):
        result=specialPythagoreanTriple.pythagoreanTripleWithSum(1000)
        self.assertEqual(result, 31875000)

if __name__=="__main__":
    unittest.main()
