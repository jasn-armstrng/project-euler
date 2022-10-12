# Question: PE4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product
# of two 3-digit numbers

def largest_palindrome(n: int) -> int:
    '''Returns the largest palidrome made from any two n-digit integers.'''
    upper_bound = (10**n)-1
    lower_bound = (10**(n-1))-1
    largest_ = 0

    for i in range(upper_bound, lower_bound, -1):
        for j in range(i, lower_bound, -1):
            product = str(i*j)
            if product == product[::-1]:
                largest_ = max(largest_, i*j)

    return largest_
