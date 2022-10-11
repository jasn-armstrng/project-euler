# Question:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
from math import sqrt, floor

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

def largestPrimeFactorOf(x:int)->int:
    largestPrimeFactor=0
    divisor=1
    while (divisor**2)<x:
        divisor+=2
        if x%divisor==0 and isPrime(divisor):
            largestPrimeFactor=divisor
    return largestPrimeFactor
