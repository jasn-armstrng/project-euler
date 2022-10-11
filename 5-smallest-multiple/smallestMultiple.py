# Question:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers
# from 1 to 20?

# Compute gcd using Euclidean algorithm
def gcd(x:list)->int:
    mod=x[1]
    while mod>0:
        gcd=x[1]
        x=[x[1],x[0]%x[1]]
        mod=x[1]
    return gcd

# Compute lcm using lcm(a,b)=(a*b)//gcd(a,b)
def lcm(x:list)->int:
    # len(x) should have at least 2
    n = len(x)
    a=x[1] # set a to first array value
    for i in range(0, len(x)):
        if i > len(x)-2:
            break
        else:
            b = x[i+1]
            res=(a*b)//gcd([a,b])
            a=res
    return a

# To do: Create a unit test for functions w/ below
# ------------------------------------------------
# Test gcd
# print(gcd([48, 18]))
# print(gcd([18, 48]))
# print(gcd([1, 2]))
# print(gcd([2, 4]))

# Test lcm
#print(lcm([i for i in range(1, 1)]))
# print(lcm([i for i in range(1, 5)]))
# print(lcm([i for i in range(1, 7)]))
# print(lcm([i for i in range(1, 21)]))
# print(lcm([i for i in range(1, 1001)]))
