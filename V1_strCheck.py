'''V1_strCheck.py'''

def strCheck(question):
    '''checks if string is not empty and only made up of letters'''
    str = input(question)
    while True:
        if len(str) > 0 and str.isalpha():
            break
        else:
            print('Please enter a valid string')
            str = input(question)
    return str

def cards_intCheck(question):
    '''checks if integer allowed to be card value, between 1-25'''
    int = input(question)
    while True:
        try:
            int = int(int)
            if 0 < int <= 25:
                break
            else:
                print('Please enter a valid integer')
                int = input(question)
        except ValueError:
            print('Please enter an integer')
            int = input(question)
    return int