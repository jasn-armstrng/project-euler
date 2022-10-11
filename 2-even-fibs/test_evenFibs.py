import unittest
import evenFibs

class TestEvenFibs(unittest.TestCase):
    def test_evenFibs(self):
        result=evenFibs.even_fibs_below(4000001)
        self.assertEqual(result, 4613732)

if __name__=="__main__":
    unittest.main()
