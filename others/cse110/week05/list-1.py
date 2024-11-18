shopping_list = []
print('Please enter the iems of the shopping list (type: quit to finish): ')

items = ''
while items.lower() != 'quit':
    items = input('Items: ').capitalize()
    if items.lower() != 'quit':
        shopping_list.append(items)

print('\nThe shopping list is:')
for items in shopping_list:
    print(items)

print('\nThe shopping list with indices is: ')
for i in range(len(shopping_list)):
    items = shopping_list[i]
    print(f'{i}. {items}')

print()
index = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ').capitalize()

shopping_list[index] = new_item

print('\nThe shopping list with indices is: ')
for i in range(len(shopping_list)):
    items = shopping_list[i]
    print(f'{i}. {items}')