#Check if element exists in list in Python
def elementexists(arr,d):
    return (d in arr)
arr = [23,32,5434,342,2,43,34,232,434]
d= int(input('enter the element you want to check:'))
print(elementexists(arr,d))
