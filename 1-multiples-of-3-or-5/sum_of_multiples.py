# Question: PE 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(int_1: int, int_2: int, limit: int) -> int:
    '''Returns the sum of all the multiples of 2 +ve integers less than a +ve integer limit.'''
    sum_of_multiples = 0

    for i in range(min(int_1, int_2), limit):
        if i%int_1 == 0 or i%int_2 == 0:
            sum_of_multiples += i

    return sum_of_multiples
