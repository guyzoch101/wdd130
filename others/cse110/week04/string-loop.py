# word = 'my name'
# favourite_letter = input('What is your favourite letter? ').lower()
# for letter in word:
#     if letter == favourite_letter:
#         print('_', end='')
#     else:
#         print(letter, end='')

start = input("Welcome to the word guessing game. To start, please press 'ENTER'")

answer = 'football'
print('Your hint is: ', end='')
for letter_answer in answer:
    print('_', end=' ')

attempts = 0

guess = input('\nWhat is your guess? ').lower()