#Python program to print even numbers in a list
def evenlist(arr,n):
    ele = []
    for i in range(0,n):
        if arr[i]%2 == 0:
            #print(arr[i],end = ' ')
            ele.append(arr[i])
    return ele
n = int(input('Enter the size of the list: '))
arr = []
arr = list(map(int,input('Enter the eements: ').strip().split()))[:n]
print( evenlist(arr,n) )