'''V1_strCheck.py'''

def str_check(question):
    '''checks if string is not empty and only made up of letters'''
    str = input(question)
    while True:
        if len(str) > 0 and str.isalpha():
            break
        else:
            print('Please enter a valid string')
            str = input(question)
    return str

def card_intcheck(question):
    '''checks if integer allowed to be card value, between 1-25'''
    num = input(question)
    while True:
        try:
            num = int(num)
            if 0 < int <= 25:
                break
            else:
                print('Please enter an integer between 1 and 25')
                num = input(question)
        except ValueError:
            print('Please enter an integer')
            num = input(question)
    return num