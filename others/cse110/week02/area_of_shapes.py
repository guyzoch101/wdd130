side_length_square = input('What is the length of a side of the square in centimetres? ')
area_square_cm = float(side_length_square) ** 2
area_square_m = area_square_cm / 10000

import math
area_circle_of_square = float(side_length_square) ** 2 * math.pi

volume_cube = float(side_length_square) ** 3

volume_sphere = 4/3 * math.pi * (float(side_length_square) ** 3)

print(f'\nThe area of the square is: {area_square_cm:.4f} cm^2 or {area_square_m} m^2')
print(f'\nThe area of the circle with its radius equals to the side length of the square is: {area_circle_of_square:.4f} cm^2')
print(f'\nThe volume of the cube is: {volume_cube:.4f} cm^3')
print(f'\nThe volume of the sphere is: {volume_sphere:.4f} cm^3')

print()
length_rectangle = input('What is the length of the rectangle in centimetres? ')
width_rectangle = input('What is the width of the rectangle in centimetres? ')
area_rectangle_cm = float(length_rectangle) * float(width_rectangle)
area_rectangle_m = area_rectangle_cm / 10000
print(f'\nThe area of the rectangle is: {area_rectangle_cm:.4f} cm^2 or {area_rectangle_m} m^2')

print()
radius_circle = input('What is the radius of the circle in centimetres? ')
import math
area_circle_cm = float(radius_circle) ** 2 * math.pi
area_circle_m = area_circle_cm / 10000
print(f'\nThe area of the circle is: {area_circle_cm:.4f} cm^2 or {round(area_circle_m, 4)} m^2')
# for rounding off values, :.4f = round(xxx, 4)