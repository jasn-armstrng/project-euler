import unittest
from largest_palindrome_product import largest_palindrome

class TestLargestPalindromeProduct(unittest.TestCase):

    def test_largest_palindrome(self):
        result = largest_palindrome(2)
        self.assertEqual(result, 9009)

        result = largest_palindrome(3)
        self.assertEqual(result, 906609)


if __name__ == "__main__":
    unittest.main()
