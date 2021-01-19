# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module

import cmath

# a = 1
# b = 5
# c = 6
a = float(input('Enter value of a: '))
b = float(input('Enter value of b: '))
c = float(input('Enter value of c: '))

# calculate the discriminant
d = (b*b)-(4*a*c)

# two solutions

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The two solutions of the quadratic equation are {0} and {1}.'.format(sol1,sol2))
