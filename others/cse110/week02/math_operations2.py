# converting degree Fahrenheit to degree Celsius
temperature_F = input('What is the temperature in Fahrenheit? ')
temperature_C = (float(temperature_F) - 32) * 5/9
print(f'The temperature in Celsius is {temperature_C:.1f} degrees.')