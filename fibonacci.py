def fibonacci(n):
    t,a,b=0,0,1#initializing the first value and second value
    if n==1:
        print(a)
    elif n== 2:
        print(b)
    else:
     print(a)
     print(b)
     for i in range(1,n-1):
           t=a+b
           a=b
           b=t
           print(t)
num = int(input('Enter no of fibonacci numbers :'))
fibonacci(num)
