# Python3 code to demonstrate
# Remove empty List from List

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

#method 1
#res = [ele for ele in test_list if ele != []]

#Method 2
res = list(filter(None,test_list))



#printing result
print("List after empty list removal : ", str(res))
