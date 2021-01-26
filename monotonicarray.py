def ismonotonic(arr,n):
     return (all(arr[i]<=arr[i+1] for i in range(len(arr)-1)) or all(arr[i]>=arr[i+1] for i in range(len(arr)-1)))
n = int(input("Enter the size of the array: "))
arr = []
arr = list(map(int,input('Enter the array elements: ').strip().split()))[:n]
print(ismonotonic(arr,n))