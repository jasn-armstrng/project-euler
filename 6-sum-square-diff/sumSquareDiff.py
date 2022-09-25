# Quesion: https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumSquareDiff(x):
    n=x+1
    sumSquares=0
    sumUpToX=0

    for i in range(1,n):
        sumUpToX+=i
        sumSquares+=(i**2)

    return (sumUpToX**2)-(sumSquares)

if __name__=='__main__':
    print(sumSquareDiff(100)) # 25164150
