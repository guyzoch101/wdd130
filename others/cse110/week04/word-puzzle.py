# an 'Enter' start button
# random function for different words in each game
# attempts limited to 5
# zip is used to consider 2 variables in a for loop
# a little if else condition in the end to handle the situation of ending the game with only 1 attempt
# a while loop for the whole program is set up as a 'Play again' button

print('Welcome to the word guessing game.')
print('You have 5 chances to guess the word.')
print('If the hint returns with a capital letter, it means the letter is in the word and in the correct position. ')
print('If the hint returns with a lowercase letter, it means the letter is in the word but in the wrong position. ')
start = input("\nTo start, please press 'ENTER' ")

play_again = 'yes'
while play_again == 'yes':
    import random
    word_list = ['football', 'locker', 'colour', 'church', 'laptop', 'rubbish', 'spaghetti', 'market', 'calculus', 'music', 'clever', 'marvel', 'solar', 'clash', 'country', 'ticket']
    secret_word = random.choice(word_list)
    print('\nYour hint is: ', end='')
    for letter_secret_word in secret_word:
        print('_', end=' ')
    attempts = 0

    if attempts <=5:
        guess = input('\nWhat is your guess? ').lower()
        attempts = attempts + 1

    while guess != secret_word and len(secret_word) == len(guess) and attempts <=5:
        while guess != secret_word and attempts <= 5 and len(secret_word) == len(guess):
            print('Your guess was not correct. ')
            print('Your hint is: ', end='')
            
            for letter_secret_word, letter_guess in zip(secret_word, guess):
                if letter_secret_word == letter_guess:
                    print(letter_secret_word.upper(), end=' ')
                elif letter_guess in secret_word:
                    print(letter_guess.lower(), end=' ')
                else:
                    print('_', end=' ')
                
            guess = input('\nWhat is your guess? ').lower()
            attempts = attempts + 1
    if attempts > 5:
        print('You have reached maximum attempts. Please try again.')
        play_again = input('\nPlay again? (yes / no) ').lower()
        break
        
    if attempts <= 5 and secret_word.lower() == guess.lower():
        print('Congratulations! You guessed it.')

        if attempts == 1:
            print(f'It took you 1 guess.')
        else:
            print(f'It took you {attempts} guesses.')
        play_again = input('\nPlay again? (yes / no) ').lower()
        break

    while len(secret_word) != len(guess):
        if attempts > 5:
            print('You have reached maximum attempts. Please try again.')
            play_again = input('\nPlay again? (yes / no) ').lower()
            break
        elif attempts <= 5:
            print('Sorry, the guess must have the same number of letters as the secret word.')
            attempts = attempts + 1
            guess = input('What is your guess? ').lower()

        while len(secret_word) == len(guess):
            if attempts > 5:
                print('You have reached maximum attempts. Please try again.')
                play_again = input('\nPlay again? (yes / no) ').lower()
                break

            while guess != secret_word and attempts <= 5 and len(secret_word) == len(guess):
                print('Your guess was not correct. ')
                print('Your hint is: ', end='')
                
                for letter_secret_word, letter_guess in zip(secret_word, guess):
                    if letter_secret_word == letter_guess:
                        print(letter_secret_word.upper(), end=' ')
                    elif letter_guess in secret_word:
                        print(letter_guess.lower(), end=' ')
                    else:
                        print('_', end=' ')
                    
                guess = input('\nWhat is your guess? ').lower()
                attempts = attempts + 1
            
            if attempts <= 5 and secret_word.lower() == guess.lower():
                print('Congratulations! You guessed it.')

                if attempts == 1:
                    print(f'It took you 1 guess.')
                else:
                    print(f'It took you {attempts} guesses.')
                play_again = input('\nPlay again? (yes / no) ').lower()
                break