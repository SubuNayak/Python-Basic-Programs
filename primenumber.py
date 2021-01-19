#python program to print prime numbers
start = 2
end = 286
for i in range(start,end):
    if i>1:
        for j in (2,i):
            if (i%j == 0):
                break
            else:
              print(i)