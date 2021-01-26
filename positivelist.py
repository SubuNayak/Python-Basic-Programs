#Python program to print positive numbers in a list
def positivelist(lst,n):
    for i in range(0,n):
        if lst[i]>=0:
            print(lst[i],end=', ')
n = int(input("Enter the size of list: "))
lst =[]
lst = list(map(int,input('Enter the elements: ').strip().split()))[:n]
print(positivelist(lst,n))