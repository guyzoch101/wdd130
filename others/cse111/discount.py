'''You work for a retail store that wants to increase sales on Tuesday and Wednesday,
which are the store’s slowest sales days. On Tuesday and Wednesday,
if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
'''

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()
subtotal = 1
while subtotal != 0:
    subtotal = float(input('Please enter the subtotal: $'))
    if subtotal == 0:
        print('Have a nice day!')
        break
    # if day_of_week in {1 ,2}...
    if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
        subtotal_discounted = 0.9 * subtotal
        
        discount_amount = subtotal - subtotal_discounted
        sales_tax = subtotal_discounted * 0.06
        total = subtotal_discounted + sales_tax
        print(f'Discount amount: ${discount_amount:.2f}')
    else:
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax
        if day_of_week == 1 or day_of_week == 2:
            difference = 50 - subtotal
            print(f'Additional amount to be purchased to receive the discout: ${difference:.2f}')

    print(f'Sales tax amount: ${sales_tax:.2f}')
    print(f'Total: ${total:.2f}')