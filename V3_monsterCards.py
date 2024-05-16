'''V1_monsterCards.py
main program that calls other functions'''
import sys
from V3_addCards import add_card
from V2_printCards import return_cards
from V3_searchCards import search_cards
from V3_removeCard import remove_card
from V1_strCheck import *

def welcome():
    '''prints welcome message to user'''
    print('Welcome to monster cards!')
    choice = intcheck('What would you like to do?\n[1] Add card\n[2] Search for Cards\n'
                      '[3] Delete Card\n[4] Print all cards\n[5] Exit\n', 1, 4)
    if choice == 1:
        name = str_check('What is the name of your card you would like to add?\n')
        print(add_card(name))
    elif choice == 2:
        name = input('What is the name of the card you would like to search for')
        print(search_cards(name))
    elif choice == 3:
        name = input('What is the name of the card you would like to remove')
        print(remove_card(name))
    elif choice == 4:
        print(return_cards())
    else:
        print('Goodbye!')
        sys.exit()

welcome()
