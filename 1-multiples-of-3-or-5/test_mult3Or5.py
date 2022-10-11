import unittest
import mult3Or5

class TestMult3Or5(unittest.TestCase):
    def test_mult3Or5(self):
        result=mult3Or5.sumOfMultiples(3,5,1000)
        self.assertEqual(result,233168)

if __name__=="__main__":
    unittest.main()
