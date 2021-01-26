#Python program that rotates the array elements d place ahead
def arrrotate(arr,d):
   # temp = arr[0]
    #for j in range(1,n):
       # if d<n:
       #  arr[j-1]=arr[d]
       #  d+=1
    #arr[n-1] = temp
   # return arr
   lst = []
   lst = arr[d:]+arr[:d]
   return lst
arr = []

d = int(input('Enter the no of places you want to shift: '))
n = int(input('Enter the size of the array'))
print('Enter the Elements of the array')
for i in range(0,n):
    ele = int(input())
    arr.append(ele)
print('Array elements after rotation :', arrrotate(arr,d))