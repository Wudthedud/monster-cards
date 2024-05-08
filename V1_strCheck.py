'''V1_strCheck.py
checks if string is not empty and is only made up of letters'''

def strCheck(question):
    str = input(question)
    while True:
        if len(str) > 0 and str.isalpha():
            break
        else:
            print('Please enter a valid string')
            str = input(question)
    return str

def cards_intCheck(question):
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