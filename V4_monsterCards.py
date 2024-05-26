'''V4_monsterCards.py
main program that calls other functions'''
import sys
import easygui as eg
from V4_addCards import add_card
from V4_printCards import return_cards
from V4_searchCards import search_card
from V4_removeCard import remove_card

# def welcome():
#     '''prints welcome message to user'''
#     print('Welcome to monster cards!')
#     choice = intcheck('What would you like to do?\n[1] Add card\n[2] Search for Cards\n'
#                       '[3] Delete Card\n[4] Print all cards\n[5] Exit\n', 1, 4)
#     if choice == 1:
#         name = str_check('What is the name of your card you would like to add?\n')
#         print(add_card(name))
#     elif choice == 2:
#         name = str_check('What is the name of the card you would like to search for')
#         print(search_cards(name))
#     elif choice == 3:
#         name = str_check('What is the name of the card you would like to remove')
#         print(remove_card(name))
#     elif choice == 4:
#         print(return_cards())
#     else:
#         print('Goodbye!')
#         sys.exit()

def input_check(question):
    """template for questions in main program"""
    name = eg.enterbox(f'What is the name of the card you would like to {question}?')
    if name is not None:
        return name
    else:
        eg.msgbox("Operation cancelled", f"{question.capitalize()} card")
        return False

def main():
    '''welome message converted to easygui'''
    while True:
        choice = eg.buttonbox('Welcome to Monster Cards Catalogue\n'
                            'What would you like to do?', 'Welcome',
                            ('Add card', 'Remove card', 'Search for card', 'Print cards', 'Exit'))
        if choice == 'Add card':
            name = input_check('add')
            if name is not False:
                add_card(name)
        elif choice == 'Remove card':
            name = input_check('remove')
            if name is not False:
                add_card(name)
            else:
                eg.msgbox("Operation cancelled", "Remove Card")
        elif choice == 'Search for cards':
            name = input_check('search for')
            if name is not False:
                search_card(name)
        elif choice == 'Print cards':
            return_cards()
        elif choice == 'Exit':
            eg.msgbox('Goodbye')
            sys.exit()

if __name__ == "__main__":
    main()
