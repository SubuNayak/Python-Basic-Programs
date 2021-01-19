#python program to find factorial of a number
#def factorial(n):
 #   if n==0:
  #      return 1
   # else:
    #    return n*factorial(n-1)


#Recursive(one line solution)

#def factorial(n):
#    return 1 if (n==1 or n==0) else n * factorial(n-1)



#Iterative(Set of statements are repeated)

def factorial(n):
    if n < 0:
      return 0
    elif n == 0 or n == 1:
        return 1
    else :
        f  = 1
        while(n>1):
            f *=n
            n-=1
        return f
num = int(input("Enter a number to find factorial: "))
fact=factorial(num)
print("Factorial of a number is ", fact  )

