# Question:
# A palindromic number reads the same both ways.
# The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product
# of two 3-digit numbers

# Solution is O(n^2)
def largestPalindrome():
    lp=0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            product = str(i * j)
            if product==product[::-1] and i*j>lp:
                lp=i*j
    return lp

if __name__=='__main__':
    print(largestPalindrome())
