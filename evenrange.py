#Python program to print even numbers in range
def evenrange(s,e):
    for i in range(s,e):
        if i%2 == 0:
             print(i,end = ' ')
s = int(input('start: '))
e = int(input('end: '))
print( evenrange(s,e) )