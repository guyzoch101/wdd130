# a name is added at the beginning
# a check out option and a payment option is added
# a receipt is added if proceed to check out
# a return loop added if invalid choice entered in the menu page

name = input('Hey dear customer! What is your name? ').capitalize()
print(f"Welcome to {name}'s Shopping Cart!")
status = True
item_list = []
price_list = []
sum_display = 0
sum = 0

while status:
    print('\nPlease select one of the following:')

    menu_list = ['Add item', 'View cart', 'Remove item', 'Compute total', 'Check out', 'Quit']
    for i in range(len(menu_list)):
        menu_options = menu_list[i]
        print(f'{i + 1}. {menu_options}')

    action = int(input('Please enter an action: '))

    if action == 1:
        item = input('What item would you like to add? ').capitalize()
        item_list.append(item)
        price = float(input(f'What is the price of {item}? $'))
        price_list.append(price)
        print(f"'{item}' has been added to the cart.")
        status = True

    elif action == 2:
        print('The contents of the shopping cart are:')
        for (item, price_display, j) in zip(item_list, price_list, range(len(item_list))):
            print(f'{j + 1}. {item} - ${price_display:.2f}')
        status = True

    elif action == 3:
        remove_item = int(input('What item would you like to remove? '))
        if remove_item > len(item_list) or remove_item > len(price_list):
            print('Sorry, that is not a valid item number.')
        else:
            item_list.pop(remove_item - 1)
            price_list.pop(remove_item - 1)
            print('Item removed.')
        status = True
    
    elif action == 4:
        for individual_price in price_list:
            sum_display += float(individual_price)
        print(f'The total price of the items in the shopping cart is ${sum_display:.2f}')
        status = True

    elif action == 5:
        if item_list == [] or price_list == []:
            print('Your cart is empty, please fill your cart first.')
            status = True
        else:
            for individual_price in price_list:
                sum += float(individual_price)
            tax = float(input('What is the sales tax percentage? '))
            checkout_total = round(sum * (1 + tax / 100), 2)
            print(f'The total amount is ${checkout_total:.2f}')
            paid_amount = 0
            
            while paid_amount < checkout_total:
                paid_amount = round(float(input('Amount paid: $')), 2)
                if paid_amount >= checkout_total:
                    change = paid_amount - checkout_total
                    print(f'Your change is ${change:.2f}')
                    print('Thank you for shopping here. Have a nice day.')
                    status = False
                    break
            
            if not status:    
                print('\nHere is your receipt:')
                print('XYZ Market')
                print(f'\nCustomer: {name}\n')
                for (item, price_display, j) in zip(item_list, price_list, range(len(item_list))):
                    print(f'{j + 1}. {item} - ${price_display:.2f}')
                print(f'Items purchased: {len(item_list)}')
                
                print(f'\nSubtotal: ${sum:.2f}')
                print(f'Sales tax {tax:.2f}%: ${round(sum * tax / 100, 2):.2f}')
                print(f'Total (Inc. tax): ${checkout_total:.2f}')
                
                print(f'\nAmount paid: ${paid_amount:.2f}')
                print(f'Change: ${change:.2f}')
                break
    
    elif action == 6:
        print('Thank you. Goodbye.')
        status = False
        break
    
    else:
        print('Invalid option. Please choose again.')
        status = True