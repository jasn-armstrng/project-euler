import unittest
from sum_square_diff import diff

class TestSumSquareDiff(unittest.TestCase):

    def test_diff(self):
        '''Test case for the diff funtion.'''
        result = diff(4)
        self.assertEqual(result, 70)

        result = diff(100)
        self.assertEqual(result, 25164150)


if __name__ == '__main__':
    unittest.main()
