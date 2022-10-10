# Question: PE 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
from math import floor, sqrt

def isPrime(x):
    # The range is based on the fact that a composite number must have a factor
    # less than or equal to the square root of that number. Otherwise, the
    # number is prime.
    if x>1:
        for i in range(2,floor(sqrt(x)+1)):
            if x%i==0:
                return False
    else:
        return False
    return True


def sumPrimesTo(n):
    sum=2
    for i in range (1,n,2):
        if isPrime(i):
            sum+=i
    return sum
