def sumofcubes(n):
    sc = 0
    for i in range(0,n+1):
        sc+= i**3
    return sc
num = int(input('Enter number:'))
print(sumofcubes(num))