def sumlist(lst):
    return sum(lst)
n = int(input('enter the size of list: '))
lst =[]
lst=list(map(int,input('Enter the elements: ').strip().split()))[:n]
print(sumlist(lst))