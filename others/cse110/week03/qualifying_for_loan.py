print('For the following questions, answer from a rating of 1-10.')
loan = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

if loan >= 5:
    if credit_history >= 7 and income >= 7:
        loan_decision = True
    
    elif credit_history >=7 or income >= 7:
        if down_payment >= 5:
            loan_decision = True
        else:
            loan_decision = False
            
    else:
        loan_decision = False

else:
    if credit_history < 4:
        loan_decision = False
    
    else:
        if income >= 7 or down_payment >= 7:
            loan_decision = True
        elif income >= 4 and down_payment >= 4:
            loan_decision = True
        else:
            loan_decision = False
            
if loan_decision:
    print('Loan is approved.')
if not loan_decision:
    print('Loan is not approved. ')