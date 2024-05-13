'''V1_monsterCards.py
main program that calls other functions'''
import sys
from V2_addCards import add_card
from V2_printCards import return_cards
from V2_searchCards import search_cards

def welcome():
    '''welcome()
    prints welcome message to user'''
    print('Welcome to monster cards!')
    choice = int(input(
          'What would you like to do?\n'
          '[1] Add card\n[2] Search for Cards\n'
          '[3] Delete Card\n[4] Print all cards\n[5] Exit\n'))
    if choice == 1:
        name = input('What is the name of your card you would like to add?\n')
        add_card(name)
    elif choice == 2:
        name = input('What is the name of the card you would like to search for')
        search_cards(name)
    elif choice == 3:
        name = input('What is the name of the card you would like to remove')
        remove_card(name)
    elif choice == 4:
        return_cards()
    else:
        print('Goodbye!')
        sys.exit()

welcome()
