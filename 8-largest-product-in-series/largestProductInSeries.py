# Ques: Project Euler ques 8.
# Given a positive number length n and positive number K find the maximum product of any contiguous subarray of size K.

import math

def largestProduct(K=int,number=int):
    strNum=str(number)
    window=[]
    maxProduct=0

    for i in range(len(strNum)):
        window.append(int(strNum[i]))

        if i>=K-1:
            maxProduct=max(maxProduct,math.prod(window))
            window.pop(0)

    return maxProduct
