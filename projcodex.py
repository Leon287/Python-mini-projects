import math
option =0
while option!=5:
    print('======================\nArea Calculator\n======================')
    option = int(input('Choose the shape: \n1)Square \n2)Rectangle \n3)Triangle \n4)Circle \n5)Exit\n\nWhich shape: '))
    if option ==1:
        print('You have choosen Square')
        side = int(input('Enter the side of the Square: '))
        area = side*side
        print(f'Area of the Square is: {area}\n')
    elif option ==2:
        print('You have choosen Rectangle')
        length = int(input('Enter the length of the Rectangle: '))
        width = int(input('Enter the width of the Rectangle: '))
        area = length*width
        print(f'Area of the Rectangle is: {area}\n')
    elif option ==3:
        print('You have choosen Triangle')
        height = int(input('Enter the height of the Triangle: '))
        base = int(input('Enter the base of the Triangle: '))
        area = 0.5*height*base
        print(f'Area of the Triangle is: {area}\n')
    elif option ==4:
        print('You have choosen Circle')
        radius = int(input('Enter the radius of the Circle: '))
        area = math.pi*(radius**2)
        print(f'Area of the radius is: {area} \n')