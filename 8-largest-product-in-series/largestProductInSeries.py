# Ques: Project Euler ques 8.
# Given a positive number length n and positive number K find the maximum product of any contiguous subarray of size K.

def largestProduct(K, number):
    strNum=str(number)
    maxProduct=1
    windowProduct=1
    windowStart=0
    print("strNum: {}".format(strNum))
    for windowEnd in range(len(strNum)):
        windowProduct*=int(strNum[windowEnd])
        print("windowProduct: {}".format(windowProduct))

        if windowEnd>=K-1:
            maxProduct=max(maxProduct,windowProduct)
            print("windowProduct, maxProduct: {}, {}".format(windowProduct, maxProduct))
            outgoingVal=int(strNum[windowStart])
            print("outVal: {}".format(outgoingVal))
            # From here can't handle zero, need to update the algo
            windowProduct/=outgoingVal
            windowStart+=1

def main():
    print("Test 1")
    largestProduct(3, 731671)
    print("-----------------------------------------------------------------------------")
    print("Test 2")
    largestProduct(3, 730671) # fails because there's a division by 0 here - windowProduct/=outgoingVal

main()
