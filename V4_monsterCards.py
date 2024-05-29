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
    while True:
        user_input = eg.enterbox(f'What is the name of the card you would like to {question}?',
                           f"{question.capitalize()} card")
        if user_input == "":
            retry = eg.ynbox('This field cannot be empty\nTry again?', f"{question.capitalize()} card")
            if not retry:
                eg.msgbox("Operation cancelled", f"{question.capitalize()} card")
                return None
        elif user_input is None:
            eg.msgbox("Operation cancelled", f"{question.capitalize()} card")
            return None
        elif not user_input.isalpha():
            retry = eg.ynbox('This field can only contain alphabetic characters\nTry again?',
                             f"{question.capitalize()} card")
            if not retry:
                eg.msgbox("Operation cancelled", f"{question.capitalize()} card")
                return None
        else:
            return user_input.lower().strip()

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
                remove_card()
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

#TODO add instructions