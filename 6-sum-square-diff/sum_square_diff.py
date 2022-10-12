# Quesion: PE6
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

def diff(range_: int) -> int:
    '''Return the difference between the sum of the square and
    square of the sum of all number up to input'''
    n = range_ + 1
    sum_of_squares = 0
    sum_of_range = 0

    for i in range(1, n):
        sum_of_range += i
        sum_of_squares += i**2

    return (sum_of_range ** 2) - sum_of_squares
