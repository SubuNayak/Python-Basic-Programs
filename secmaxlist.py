#Python program to find second largest number in a list
arr = [3,4,4,5,6,7,8,9,10]

#method 1
#print(sorted(arr)[-2])

#method 2
#arr.sort()
#print(arr[-2])

#method 3
new_arr = set(arr)
new_arr.remove(max(new_arr))
print(max(new_arr))