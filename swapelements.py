def swapelements(arr,p1,p2):
    arr[p1-1] , arr[p2-1] = arr[p2-1] , arr[p1-1]
    return arr
n = int(input('Enter the size of the array: '))
arr = []
arr = list(map(int,input('Enter the elements: ').strip().split()))[:n]
p1 = int(input('Enter the first position: '))
p2 = int(input('Enter the second position: '))
print(swapelements(arr,p1,p2))