#Python program to interchange first and last elements in a list
def interchange(arr,n):
    arr[0] , arr[n-1] = arr[n-1] , arr[0]
    return arr
n = int(input('Enter the size of the array: '))
arr= []
arr = list(map(int,input('Enter the elements: ').strip().split()))[:n]
print(interchange(arr,n))