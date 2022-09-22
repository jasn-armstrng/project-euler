# Question
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from math import floor, sqrt

primes = []

def isPrime(x):
    # The range is based on the fact that a composite number must have a factor
    # less than or equal to the square root of that number. Otherwise, the
    # number is prime.
    prime=True

    if x>1:
        for i in range(2,floor(sqrt(x)+1)):
            if x%i==0:
                prime = False
                break
    return prime


for i in range(2, 20):
    if isPrime(i):
        primes.append(i)

print(primes)
