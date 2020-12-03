x = int(input(' Press 1 for area of rectangle: \n Press 2 for area of square: \n Press 3 for area of circle: \n Press 4 to exit \n'))

while (x<=4):
    if (x==1):
        a = int(input('Enter Length of Rectangle: '))
        b = int(input('Enter Breadth of Rectangle: '))
        areaRectangle = a*b
        print('Area of Rectangle = ', areaRectangle)
        continue
    elif (x==2):
        s = int(input('\nEnter Sides of Square: '))
        areaSquare = s**2
        print('Area of Square = ', areaSquare)
    elif (x==3):
        r = int (input('\nEnter Radius of the Circle: '))
        areaCircle = 3.14*r*r
        print('Area of Circle = ', areaCircle)
    elif (x==4):
        exit()