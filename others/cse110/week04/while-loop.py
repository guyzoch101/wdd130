positive_number = int(input('Please type a positive number: '))

while positive_number < 0:
    print('Sorry, that is a negative number. Please try again.')
    positive_number = int(input('Please type a positive number: '))
    
print(f'The number is: {positive_number}')

candy = input('May I have a piece of candy? ')

while candy.lower() == 'no':
    candy = input('May I have a piece of candy? ')
    
if candy.lower() == 'yes':
    print('Thank you.')

# alternative:
# answer = ''
#
# while answer != 'yes':
#   answer = input('May I have a piece of candy? ')
#
# print('Thank you.')
#
# different style: enter while loop when the answer is not yes
# consider what leads the loop to break, then decide the condition of the loop