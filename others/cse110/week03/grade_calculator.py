grade_percentage = int(input('What is your grade percentage? '))

last_digit = grade_percentage % 10
sign = ''

print()

if grade_percentage >= 90:
    letter_grade = 'A'
elif grade_percentage >= 80 and grade_percentage < 90:
    letter_grade = 'B'
elif grade_percentage >= 70 and grade_percentage < 80:
    letter_grade = 'C'
elif grade_percentage >= 60 and grade_percentage < 70:
    letter_grade = 'D'
else:
    letter_grade = 'F'

if letter_grade == 'A':
    if last_digit < 3:
        sign = '-'
    else:
        sign = ''

elif letter_grade == 'F':
    sign = ''

else:
    if last_digit >= 7:
        sign = '+'
    elif last_digit < 3:
        sign = '-'
    else:
        sign = ''

print(f'Your letter grade is {letter_grade}{sign}. ')

if grade_percentage >= 70:
    print('Congratulations! You passed! ')
# double quotes are used due to apostrophe
else:
    print("Don't give up. You'll do better next time.")