# Question: PE3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

from math import floor, sqrt

def is_prime(int_: int) -> bool:
    """
    Checks if input is prime and returns True/False.

    The check is based on the fact that a composite number must have a factor less than
    or equal to the square root of that number. Otherwise, the number is prime.
    """
    if int_ > 1:
        for i in range(2, floor(sqrt(int_) + 1)):
            if int_ % i == 0:
                return False
    else:
        return False

    return True


def largest_prime_factor(int_: int) -> int:
    '''
    Returns the largest prime factor of a +ve integer.

    Ugly bit to be redone:
    1. If the input turns out to be prime return input.
    2. Assign even inputs the even base prime factor - 2,
    3. Then only check odd numbers as possible prime factors.
    '''
    largest_ = int_

    if int_%2 == 0:
        largest_ = 2

    divisor = 1
    while (divisor ** 2) < int_:
        divisor += 2
        if int_%divisor == 0:
            if is_prime(divisor):
                largest_ = divisor

    return largest_
