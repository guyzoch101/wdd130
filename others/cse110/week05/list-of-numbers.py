print('Enter a list of numbers, type 0 when finished.')
number_list = []
number = 1
while number != 0:
    number = int(input('Enter number: '))
    if number != 0:
        number_list.append(number)

sum = int()
for variable in number_list:
    sum += int(variable)

count = len(number_list)
average = sum / count

largest = 0
for value in number_list:
    if value > largest:
        largest = value

smallest_positive = 10000
for value_positive in number_list:
    if value_positive < smallest_positive and value_positive > 0:
        smallest_positive = value_positive

sorted_list = sorted(number_list)

print(f'The sum is: {sum}')
print(f'The average is: {average}')
print(f'The largest number is: {largest}')
print(f'The smallest positive number is: {smallest_positive}')
print('The sorted list is:')
for sorting in sorted_list:
    print(sorting)