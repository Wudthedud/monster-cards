'''V2_strCheck.py
add easyGUI'''
import easygui as eg

def str_check(question, title):
    '''checks if string is not empty and only made up of letters'''
    msg = eg.enterbox(question, title)
    try:
        while True:
            if len(msg) > 0 and msg.replace(' ','').isalpha():
                return msg.lower().strip()
            if len(msg) <= 0:
                eg.msgbox('The string you entered is empty, please enter a valid string')
                msg = eg.enterbox(question, title)
            else:
                eg.msgbox(f'The string "{msg}" does not contain only alphabetic characters\n'
                        'Please make sure to enter a valid string (A-Z)')
                msg = eg.enterbox(question, title)
    except TypeError:
        return

def card_intcheck(question):
    '''checks if integer allowed to be card value, between 1-25'''
    num = input(question)
    while True:
        try:
            num = int(num)
            if 0 < num <= 25:
                break
            else:
                print('Please enter an integer between 1 and 25')
                num = input(question)
        except ValueError:
            print('Please enter an integer')
            num = input(question)
    return num

def intcheck(question, min,  ):
    num = input(question)
    while True:
        try:
            num = int(num)
            if min <= num <= max:
                break
            else:
                print(f'Please enter an integer between {min} and {max}')
                num = input(question)
        except ValueError:
            print('Please enter an integer')
            num = input(question)
    return num

print(str_check('Enter a string:', 'Test'))
