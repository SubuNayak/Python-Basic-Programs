#Python program to print odd numbers in range
def oddrange(s,e):
    for i in range(s,e+1):
        if i%2 != 0:
             print(i,end = ' ')
s ,e= int(input('start: ')),int(input('end: '))
#e = int(input('end: '))
print( oddrange(s,e) )