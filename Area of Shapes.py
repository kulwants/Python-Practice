def areaRectangle(a, b): 
    return (a * b) 
a = int(input('Enter Length of Rectangle: '))
b = int(input('Enter Breadth of Rectangle: ')) 
print('Area of Rectangle = ', areaRectangle(a, b)) 

def areaSquare(s):
    return (s * s)
s = int(input('\nEnter Sides of Square: '))
print('Area of Square = ', areaSquare(s))

def areaCircle(r):
    return (3.14 * r * r)
r = int (input('\nEnter Radius of the Circle: '))
print('Area of Circle = ', areaCircle(r))