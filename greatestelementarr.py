def maxelement(arr,n):
    max = arr[0];
    for i in range(1,n):
        if max < arr[i]:
            max = arr[i]

    return max
n = int(input('Enter the size of array: '))
arr =[]
for i in range(0,n):
    ele = int(input( ))
    arr.append(ele)
print('Greatest element in the array: ',maxelement(arr,n))
