# Question: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
from math import sqrt

def loadSquares(K:int)->dict:
    # Returns hash with integer key and its square as value
    hash={}
    for i in range(K+1):
        hash[i]=i**2
    return hash

# Brute force solution
def pythagoreanTripleWithSum(K:int)->int:
    hash=loadSquares(K)
    for a in range(1,K):
        for b in range(a+1,K+1):
            c=sqrt(hash[a]+hash[b])
            if c in hash:
                if a+b+c==K:
                    return a*b*c
