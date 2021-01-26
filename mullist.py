import numpy
def mullist(lst):
    return numpy.prod(lst)
n = int(input('enter the size of list: '))
lst =[]
lst=list(map(int,input('Enter the elements: ').strip().split()))[:n]
print(mullist(lst))