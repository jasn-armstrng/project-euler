# Question:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# -> Find the sum of all the multiples of x or y below K.

def sumOfMultiples(x:int, y:int, K:int)->int:
    sum = 0
    start=min(x,y)
    for i in range(start, K):
        if i%x==0 or i%y==0:
            sum+=i
    return sum
