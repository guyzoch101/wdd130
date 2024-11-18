# displaying 

windspeed = int()
# function for windchill formula
def windchill_formula(temperature):
    return round(35.74 + 0.6215 * temperature - 35.75 * (windspeed ** 0.16) + 0.4275 * temperature * (windspeed ** 0.16), 2)
    
temperature = float(input('What is the temperature? '))
unit = input('Fahrenheit or Celsius (F/C)? ').upper()
if unit == 'C':
    temperature_c = temperature
    temperature = temperature * 9/5 + 32
elif unit == 'F':
    temperature_c = round((temperature - 32) * 5/9, 2)

for n in range(1, 13):
    windspeed = n * 5
    windchill = windchill_formula(temperature)
    windchill_c = round((windchill - 32) * 5/9, 2)
    print(f'At temperatre {temperature}F / {temperature_c}C, and wind speed {windspeed} mph, the windchill is {windchill}F / {windchill_c}C')