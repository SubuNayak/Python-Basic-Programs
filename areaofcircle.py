#python program  to find area of a circle
def area(r):
    PI = 3.142
    return PI * ( r * r)
radius = float(input (' Enteer Radius : '))
print("Area is %.6f" %area(radius))