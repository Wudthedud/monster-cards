'''V4_monsterCards.py
main program that calls other functions'''
import sys
import easygui as eg
from V4_addCards import add_card
from V4_printCards import return_cards
from V4_searchCards import search_card
from V4_removeCard import remove_card

def input_check(question):
    """template for questions in main program"""
    user_input = eg.enterbox(f'What is the name of the card you would like to {question}?',
                       f"{question.capitalize()} card")
    if user_input is not None and user_input != "":
        return user_input
    if user_input == "":
        retry = eg.ynbox('This field cannot be empty\nTry again?', f"{question.capitalize()} card")
        if retry:
            input_check(question)
        else:
            eg.msgbox("Operation cancelled", f"{question.capitalize()} card")
            return None
    else:
        eg.msgbox("Operation cancelled", f"{question.capitalize()} card")
        return None

def main():
    '''welome message converted to easygui'''
    while True:
        choice = eg.buttonbox('Welcome to Monster Cards Catalogue\n'
                            'What would you like to do?', 'Welcome',
                            ('Add card', 'Remove card', 'Search for card', 'Print cards', 'Exit'))
        if choice == 'Add card':
            name = input_check('add')
            if name is not None:
                add_card(name)
        elif choice == 'Remove card':
            name = input_check('remove')
            if name is not None:
                remove_card(name)
        elif choice == 'Search for cards':
            name = input_check('search for')
            if name is not None:
                search_card(name)
        elif choice == 'Print cards':
            return_cards()
        elif choice == 'Exit':
            eg.msgbox('Goodbye')
            sys.exit()

if __name__ == "__main__":
    main()