# Question:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
from math import floor, sqrt

def isPrime(x:int)->bool:
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

def nthPrime(n:int)->int:
    num=1 # Number to check. Incremented in while loop
    primeCounter=0 # Tracks the number of primes found
    lastPrime=0 # The last prime found

    while primeCounter<n:
        if isPrime(num):
            primeCounter+=1
            lastPrime=num
        num+=1
    return lastPrime
