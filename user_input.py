#python program to take input from the user and store in array.
def user_input(n):
    lst=[]
    lst=list(map(int,input('Enter the elements: ').strip().split()))[:n]
    return lst
n= int(input('Enter the size ofthe array.'))
print(user_input(n))