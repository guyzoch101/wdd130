# 10% service charge is added, a tip MCQ is added, and a while loop created if one's funds can't cover the meal
# My name is used a as the name of the restaurant
# Double quotes are used due to apostrophes used in the sentence
# Rows 5 to 12 are the milestone requirements
# my notes: Remember to round when calculating to prevent deviation between stored value and displayed value
child_meal_price = float(input("The price of a child's meal: $"))
adult_meal_price = float(input("The price of an adult's meal: $"))
number_of_children = int(input('Number of children: '))
number_of_adults = int(input('Number of adults: '))

meal_subtotal = round(child_meal_price * number_of_children + adult_meal_price * number_of_adults, 2)

print(f'\nThe subtotal of the meals: ${meal_subtotal}')

sales_tax_rate = float(input('\nWhat is the percentage of sales tax? '))
sales_tax = round(sales_tax_rate / 100 * round(meal_subtotal,2), 2)
print(f'\nThe amount of sales tax to be paid: ${sales_tax}')

# 10% service charge part
print('\nThere will be a 10% service change on top of the meal subtotal.')
total_price = round(meal_subtotal * 1.1 + sales_tax, 2)
print(f'\nThe total price of the meal: ${total_price}')

# Tip MCQ part
tip_answer = input("\nWe hope you enjoyed your meals at Tristan's, how much would you like to tip us? \nA. None \nB. 5% \nC. 10% \nD. 15% \n(Enter A, B, C, or D) \n")
tip = tip_answer.capitalize()
print()

if tip == 'A':
    amount_paid = float(input('Amount paid: $'))
    change = round(amount_paid - total_price, 2)
    
    while (change < 0):
        print('The current amount is insufficient. Please prepare sufficient funds.')
        print(f'\nThe total price of the meal: ${total_price}')
        amount_paid = float(input('Amount paid: $'))
        change = round(amount_paid - total_price, 2)
        
        if (change >= 0):
            break
        
        else:
            print('The current amount is insufficient. Please prepare sufficient funds.')
            print(f'\nThe total price of the meal: ${total_price}')
            amount_paid = float(input('Amount paid: $'))

elif tip == 'B':
    total_price_b = round(total_price * 1.05, 2)
    print(f'\nThe total amount including tip will be: ${total_price_b}')
    print()
    amount_paid = float(input('Amount paid: $'))
    change = round(amount_paid - total_price_b, 2)
    
    while (change < 0):
        print('The current amount is insufficient. Please prepare sufficient funds.')
        print(f'\nThe amount including tip will be: ${total_price_b}')
        amount_paid = float(input('Amount paid: $'))
        change = round(amount_paid - total_price_b, 2)
        
        if (change >= 0):
            break
        
        else:
            print('The current amount is insufficient. Please prepare sufficient funds.')
            print(f'\nThe total amount including tip will be: ${total_price_b}')
            amount_paid = float(input('Amount paid: $'))

elif tip == 'C':
    total_price_c = round(total_price * 1.1, 2)
    print(f'\nThe total amount including tip will be: ${total_price_c}')
    print()
    amount_paid = float(input('Amount paid: $'))
    change = round(amount_paid - total_price_c, 2)
    
    while (change < 0):
        print('The current amount is insufficient. Please prepare sufficient funds.')
        print(f'\nThe total amount including tip will be: ${total_price_c}')
        amount_paid = float(input('Amount paid: $'))
        change = round(amount_paid - total_price_c, 2)
        
        if (change >= 0):
            break
        
        else:
            print('The current amount is insufficient. Please prepare sufficient funds.')
            print(f'\nThe total amount including tip will be: ${round(total_price_c, 2)}')
            amount_paid = float(input('Amount paid: $'))

elif tip == 'D':
    total_price_d = round(total_price * 1.15, 2)
    print(f'\nThe total amount including tip will be: ${total_price_d}')
    print()
    amount_paid = float(input('Amount paid: $'))
    change = round(amount_paid - total_price_d, 2)
    
    while (change < 0):
        print('The current amount is insufficient. Please prepare sufficient funds.')
        print(f'\nThe total amount including tip will be: ${total_price_d}')
        amount_paid = float(input('Amount paid: $'))
        change = round(amount_paid - total_price_d, 2)
        
        if (change >= 0):
            break
        
        else:
            print('The current amount is insufficient. Please prepare sufficient funds.')
            print(f'\nThe total amount including tip will be: ${total_price_d}')
            amount_paid = float(input('Amount paid: $'))
            
print(f'\nChange: ${change}')
print("\nThank you for coming to Tristan's. Have a nice day~")