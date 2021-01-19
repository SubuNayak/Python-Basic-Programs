def sumofsquares(n):
    ss = 0
    for i in range(0,n+1):
        ss+= i**2
    return ss
num = int(input('Enter number:'))
print(sumofsquares(num))