#Python program to find N largest elements from a list
n = int(input('Enter the size of the list: '))
lst = []
lst = list(map(int,input('Enter the eements: ').strip().split()))[:n]
d = int(input('no of largest numbers: '))
print(sorted(lst)[-d:])