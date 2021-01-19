#Python Program for How to check if a given number is Fibonacci number?
import math
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
def isFibonacci(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)
for i in range(1,12):
    if (isFibonacci(i)== True):
        print(i,'is a Fibonacci number')
    else:
        print(i,'is not a fibonacci number.')