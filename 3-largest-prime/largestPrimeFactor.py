# Question:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
from math import sqrt, floor

def is_prime(x: int) -> bool:
  """Returns True if prime else False

  Approach:
    The range is based on the fact that a composite number must have a factor
    less than or equal to the square root of that number. Otherwise, the
    number is prime.
  """
  if x > 1:
    for i in range(2, floor(sqrt(x) + 1)):
      if x % i == 0:
        return False
      else:
        return False

  return True

def largest_prime_factor_of(x: int) -> int:
  """Returns the largest prime factor

  The below is ugly
  1. If no prime factor < x return x
  2. Run a hack assigning evens the even base prime factor - 2
  3. Then only check odd numbers as possible factors
  """
  largest_prime_factor = x

  if x % 2 == 0:
    largest_prime_factor=2

  divisor = 1
  while (divisor ** 2) < x:
    divisor += 2
    if x % divisor == 0:
      if is_prime(divisor):
        largest_prime_factor = divisor

  return largest_prime_factor
