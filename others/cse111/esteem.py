'''The Rosenberg self-esteem scale is a self-esteem measure developed
    by the sociologist Morris Rosenberg in 1965. It is still used in
    social-science research today. To complete the measure, a person
    completes a survey that contains the following ten statements.'''

def display_rules():
    # printing the rules and the scores
    
    print('The person responds to each statement by choosing one of these four options: strongly disagree, disagree, agree, or strongly agree.')
    print('Corresponding points will be given to each response.')
    print('Please respond by D (= strongly disagree), d (=disagree), a (=agree), A (=strongly agree).')
    
    pass

def display_statement_1():
    print('1. I feel that I am a person of worth, at least on an equal plane with others.')
    response_1 = get_response(1)
    
    return response_1

def display_statement_2():
    print('2. I feel that I have a number of good qualities.')
    response_2 = get_response(2)
    
    return response_2

def display_statement_3():
    print('3. All in all, I am inclined to feel that I am a failure.')
    response_3 = get_response(3)
    
    return response_3

def display_statement_4():
    print('4. I am able to do things as well as most other people.')
    response_4 = get_response(4)
    
    return response_4

def display_statement_5():
    print('5. I feel I do not have much to be proud of.')
    response_5 = get_response(5)
    
    return response_5

def display_statement_6():
    print('6. I take a positive attitude toward myself.')
    response_6 = get_response(6)
    
    return response_6

def display_statement_7():
    print('7. On the whole, I am satisfied with myself.')
    response_7 = get_response(7)
    
    return response_7

def display_statement_8():
    print('8. I wish I could have more respect for myself.')
    response_8 = get_response(8)
    
    return response_8

def display_statement_9():
    print('9. I certainly feel useless at times.')
    response_9 = get_response(9)
    
    return response_9

def display_statement_10():
    print('10. At times I think I am no good at all.')
    response_10 = get_response(10)
    
    return response_10


def get_response(statement):
    # getting responses from users
    
    if statement == 1:
        print('D = strongly disagree')
        print('d = disagree')
        print('a = agree')
        print('A = strongly agree')
    
    response = input('Please respond with D, d, a, or A: ')
    
    return response

def get_score(response, statement):
    # assigning points to the corresponding response
    
    if response == 'D':
        if statement in (1, 2, 4, 6, 7):
            points = 0
        
        elif statement in (3, 5, 8, 9, 10):
            points = 3
    
    elif response == 'd':
        if statement in (1, 2, 4, 6, 7):
            points = 1
        
        elif statement in (3, 5, 8, 9, 10):
            points = 2
    
    elif response == 'a':
        if statement in (1, 2, 4, 6, 7):
            points = 2
        
        elif statement in (3, 5, 8, 9, 10):
            points = 1
    
    elif response == 'A':
        if statement in (1, 2, 4, 6, 7):
            points = 3
        
        elif statement in (3, 5, 8, 9, 10):
            points = 0
    
    return points

def main():
    display_rules()
    
    response_1 = display_statement_1()
    score_1 = get_score(response_1, 1)
    
    response_2 = display_statement_2()
    score_2 = get_score(response_2, 2)
    
    response_3 = display_statement_3()
    score_3 = get_score(response_3, 3)
    
    response_4 = display_statement_4()
    score_4 = get_score(response_4, 4)
    
    response_5 = display_statement_5()
    score_5 = get_score(response_5, 5)
    
    response_6 = display_statement_6()
    score_6 = get_score(response_6, 6)
    
    response_7 = display_statement_7()
    score_7 = get_score(response_7, 7)
    
    response_8 = display_statement_8()
    score_8 = get_score(response_8, 8)
    
    response_9 = display_statement_9()
    score_9 = get_score(response_9, 9)
    
    response_10 = display_statement_10()
    score_10 = get_score(response_10, 10)
    
    total = score_1 + score_2 + score_3 + score_4 + score_5 + score_6 \
        + score_7 + score_8 + score_9 + score_10
    
    print(f'Your score is {total}.')
    print('A score below 15 may indicate problematic low self-esteem.')
    
    pass

if __name__ == "__main__":
    main()