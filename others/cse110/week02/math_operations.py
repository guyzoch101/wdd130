age = input('How old are you? ')
age_next_year = int(age) + 1
print('On your next brithday, you will be ' + str(age_next_year))
# print(f'On your next birthday, you will be {age_next_year}')

print()
eggs_carton = input('How many egg cartons do you have? ')
eggs = int(eggs_carton) * 12
print('You have ' + str(eggs) + ' eggs')

print()
cookies = input('How many cookies do you have? ')
people = input('How many people are there? ')
answer = int(cookies) / int(people)
print('Each person may have ' + str(answer) + ' cookies')