#Python program that rotates the array elements one place ahead
def arrrotate(arr,n):
    temp = arr[0]
    for j in range(1,n):
        arr[j-1]=arr[j]
    arr[n-1] = temp
    return arr
arr = []
n = int(input('Enter the size of the array'))
print('Enter the Elements of the array')
for i in range(0,n):
    ele = int(input())
    arr.append(ele)
print('Array elements after rotation :', arrrotate(arr,n))