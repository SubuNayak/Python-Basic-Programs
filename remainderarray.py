def remainder(arr,n,d):
    mul = 1
    for i in range(0,n):
        mul *= arr[i]
    return mul%d
n = int(input('Enter the size of the Array: '))
arr = []
arr = list(map(int,input('Enter the elements of the array: ').strip().split()))[:n]
d = int(input('Enter the number with which you want to divide: '))
print('Output: ',remainder(arr,n,d))