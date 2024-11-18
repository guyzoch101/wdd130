play_again = True
while play_again:
    import random
    magic_number = random.randint(1, 100)
    guess = int(input('What is your guess? '))

    while magic_number > guess:
        if magic_number == guess:
            break
        print('Higher')
        guess = int(input('What is your guess? '))

    while magic_number < guess:
        if magic_number == guess:
            break
        print('Lower')
        guess = int(input('What is your guess? '))
        
    if magic_number == guess:
        print('You guessed it!')

    while play_again != 'yes' or play_again != 'no':
        play_again = input('\nPlay again? (yes / no) ').lower()
        if play_again == 'yes':
            play_again = True
            print()
            break
        elif play_again == 'no':
            play_again = False
            print('Thank you for playing.')
            break
        