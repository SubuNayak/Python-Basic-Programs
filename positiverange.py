#Python program to print all positive numbers in a range
def positiverange(s,e):
    for i in range(s,e+1):
        if i>=0:
            print(i,end = ', ')
s = int(input('start: '))
e = int(input('end: '))
print( positiverange(s,e) )