# Question:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
from math import sqrt, floor

def isPrime(x):
    # The range is based on the fact that a composite number must have a factor
    # less than or equal to the square root of that number. Otherwise, the
    # number is prime.
    prime=True

    if x>1:
        for i in range(2, floor(sqrt(x)+1)):
            if x%i==0:
                prime = False
                break
    return prime

def largestPrimeFactorOf(x):
    largestPrimeFactor=0
    divisor=2
    while (divisor**2)<x:
        if x%divisor==0:
            if isPrime(divisor):
                largestPrimeFactor=divisor
        divisor+=1
    return largestPrimeFactor

if __name__=='__main__':
    print(largestPrimeFactorOf(600851475143))
