def clearlist(lst):
    lst.clear()
    return lst
n = int(input('enter the size of list: '))
lst =[]
lst=list(map(int,input('Enter the elements: ').strip().split()))[:n]
print(clearlist(lst))