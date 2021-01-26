#Python program to print all negative numbers in a range
def negativerange(s,e):
    for i in range(s,e+1):
        if i<0:
            print(i,end = ', ')
s = int(input('start: '))
e = int(input('end: '))
print( negativerange(s,e) )