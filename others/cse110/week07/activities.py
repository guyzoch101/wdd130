import math
def compute_area_square(side):
    return round(side ** 2, 2)

def compute_area_rectangle(length, width):
    return round(length * width, 2)

def compute_area_circle(radius):
    return round((radius ** 2) * math.pi, 2)

status = True

while status:
    shape = input('What kind of shape do you have? ').lower()
    
    if shape == 'square':
        side = float(input('What is the side length of the square? '))
        square_area = compute_area_square(side)
        print(f'The area of the square is {square_area}')

    elif shape == 'rectangle':
        length = float(input('What is the length of the rectangle? '))
        width = float(input('What is the width of the rectangle? '))
        rectangle_area = compute_area_rectangle(length, width)
        print(f'The area of the rectangle is {rectangle_area}')

    elif shape == 'circle':
        radius = float(input('What is the radius of the circle? '))
        circle_area = compute_area_circle
        print(f'The area of the circle is {circle_area}')
    
    else:
        print('Invalid shape entered.')
    
    status = input('Enter quit to leave: ').lower()
    if status == 'quit':
        status = False
    else:
        status = True