#Python program to find largest number in a list
def maxlist(arr):
    return max(arr)
n = int(input("Enter the size of the array: "))
arr = []
arr = list(map(int,input('Enter the elements: ').strip().split()))[:n]
print(maxlist(arr))