# Tristan Wong
# 1/18/2024
# This program is about calculating the volume of space inside a tire

# import datetime and math library
from datetime import datetime
import math

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# asks for user input of width, aspect ratio and diameter of the tire
width = float(input('Please enter the width of the tire in milimeters (ex 205): '))
aspect_ratio = float(input('Please enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Please enter the diameter of the wheel in inches (ex 15): '))

# calculates the volume of the tire
volume = round((math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / (10 ** 10), 2)

# prints the volume in l
print(f'\nThe approximate volume is {volume} liters\n')

''' stretch part: using the diamemter of the tire to list out the price
and ask for customers' decision on purchasing qualities, and phone number '''
if diameter == 13:
    price = 55.99
    print(f'The price for 1 tire is ${price}')

elif diameter == 15:
    price = 88.99
    print(f'The price for 1 tire is ${price}')

elif diameter == 17:
    price = 200.99
    print(f'The price for 1 tire is ${price}')

elif diameter == 19:
    price = 265.99
    print(f'The price for 1 tire is ${price}')

elif diameter == 21:
    price = 378.99
    print(f'The price for 1 tire is ${price}')

else:
    print('Prices for your tire size is currently unavailable. Sorry for the inconvenience.')

# a decision question to ask for customers' decision
decision = input('Buy this tire? (yes/no) ').lower()
    
if decision == 'yes':
    phone_number = input('\nPlease enter your phone number for further contacting: (please enter numbers only) ')
    # opens the text file volumes.txt and enters the data
    # at means appending text
    # phone number is entered as well if the cusomter would like to buy the tire
    with open('week02/volumes.txt', 'at') as volumes_file:
        print(f'{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume}, {phone_number}', file=volumes_file)
    print('\nThank you for choosing 111Tires. Have a nice day.')
    
elif decision == 'no':
    # opens the text file volumes.txt and enters the data
    with open('week02/volumes.txt', 'at') as volumes_file:
        print(f'{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume}', file=volumes_file)
    print('\nThank you for using our services. Have a nice day.')