#Python program to print negative numbers in a list
def negativelist(lst,n):
    for i in range(0,n):
        if lst[i]<0:
            print(lst[i],end=', ')
n = int(input("Enter the size of list: "))
lst =[]
lst = list(map(int,input('Enter the elements: ').strip().split()))[:n]
print(negativelist(lst,n))