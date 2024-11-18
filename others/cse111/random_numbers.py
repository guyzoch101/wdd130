import random

def main():
    '''Parameters: none
        Return: none'''
    
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    
    '''Calling the append_random_numbers funtion with 1
        argument only, appending 1 number'''
    numbers = append_random_numbers(numbers)
    print(numbers)
    
    '''Calling the append_random_numbers function with 2
        arguments, appending 3 numbers'''
    numbers = append_random_numbers(numbers, 3)
    print(numbers)
    
    words = ["append", "new", "words"]
    print(words)
    
    '''Calling the append_random_words funtion with 1
        argument only'''
    '''Using random.randint to generate an integer with a
        range from 1 to 6, to determine the quantity of words
        to be appended into the words_list'''
    words = append_random_words(words, quantity = random.randint(1, 6))
    print(words)
    
    pass


def append_random_numbers(numbers_list, quantity = 1):
    '''Parameters:
        numbers_list for the numbers list
        quantity for the quantity of numbers to be appeneded
            into the list, with a default value of 1'''
    

    ''' index for the while loop appending the quantity
        of numbers into the list'''
    i = 1
    
    while i <= quantity:
        '''Using random.uniform to generate a random number
            between 1 and 100, with it being rounded to 1 dp'''
        number = round(random.uniform(1, 100), 1)
        
        # appending the generated number into the numbers list
        numbers_list.append(number)
        
        i += 1

    return numbers_list


def append_random_words(words_list, quantity = 1):
    '''Parameters:
        words_list for the words list
        quantity for the quantity of words to be appeneded
            into the list, with a default value of 1'''
    
    random_word_list = ['join', 'love', 'smile', 'love', 'cloud', 'head']
    
    ''' index for the while loop appending the quantity
        of words into the list'''
    i = 1
    
    while i <= quantity:
        '''Using random.choice to generate a random word from
            the random_word_list'''
        word = random.choice(random_word_list)
        
        # appending the generated word into the wordss list
        words_list.append(word)
        
        i += 1
    
    return words_list


if __name__ == "__main__":
    main()