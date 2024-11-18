first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
job_title = input('Enter your job title: ')
id = input('Enter your ID number: ')
email_address = input('Enter your email address: ')
phone_number = input('Enter your phone number: ')

#stretch part
hair_colour = input('Enter the colour of your hair: ')
eyes_colours = input('Enter the colour of your eyes: ')
month = input('Enter your month of birth: ')
training = input('Have you completed advanced training? (yes/no): ')

#note: for \n be red = nothing wrong
print('\nThe ID card is:')
print('----------------------------------------')
output = f'{last_name.upper()}, {first_name.title()}'
print(output)
print(job_title.title())
print(f'ID: {id}')
print()
print(email_address.lower())
print(phone_number)
print()

#2-column part (2nd column not alligned)
#print('{:<15} {:>15}'.format('Hair: ' + hair_colour.capitalize(), 'Eyes: ' + eyes_colours.capitalize()))
#print('{:<15} {:>15}'.format('Month: ' + month.capitalize(), 'Training: ' + training.capitalize()))
#sugguest solution for displaying output with 2 columns
print(f"Hair: {hair_colour.capitalize():15} Eyes: {eyes_colours.capitalize()}")
print(f"Month: {month.capitalize():14} Training: {training.capitalize()}")
print('----------------------------------------')