#Python program to find smallest number in a list
def minlist(arr):
    return min(arr)
n = int(input("Enter the size of the array: "))
arr = []
arr = list(map(int,input('Enter the elements: ').strip().split()))[:n]
print(minlist(arr))