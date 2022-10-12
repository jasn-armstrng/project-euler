# Question: PE5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers
# from 1 to 20?

def gcd(arr: list) -> int:
    '''Returns gcd of 2 +ve integers using a Euclidean algorithm.'''
    mod = arr[1]

    while mod > 0:
        gcd_ = arr[1]
        arr = [arr[1], arr[0]%arr[1]]
        mod = arr[1]

    return gcd_


def lcm(arr: list) -> int:
    '''Returns lcm using lcm(a,b) = (a*b)//gcd(a,b).'''
    # length of input array should be > 1
    n = len(arr) # len(x) should have at least 2
    lcm_ = arr[0] # set lcm_ to first array value

    # Sliding window
    for i in range(0, n):
        if i > n-2:
            break
        else:
            b = arr[i+1]
            res = (lcm_*b)//gcd([lcm_, b])
            lcm_ = res

    return lcm_
