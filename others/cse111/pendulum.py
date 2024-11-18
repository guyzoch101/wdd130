# Tristan Wong
# 1/10/2024
"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""

import math
height = float(input('Please enter the length of the pendulum: '))

time = 2 * math.pi * (height / 9.81) ** 0.5
# time = 2 * math.pi * math.sqrt(height / 9.81)

print(f'The time taken for the pendulum to swing back and forth is {round(time, 2)} seconds')