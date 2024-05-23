'''V4_monsterCards.py
main program that calls other functions'''
import sys
import easygui as eg
from V4_addCards import add_card
from V2_printCards import return_cards
from V3_searchCards import search_cards
from V3_removeCard import remove_card
from V1_strCheck import str_check, intcheck

def welcome():
    '''prints welcome message to user'''
    print('Welcome to monster cards!')
    choice = intcheck('What would you like to do?\n[1] Add card\n[2] Search for Cards\n'
                      '[3] Delete Card\n[4] Print all cards\n[5] Exit\n', 1, 4)
    if choice == 1:
        name = str_check('What is the name of your card you would like to add?\n')
        print(add_card(name))
    elif choice == 2:
        name = str_check('What is the name of the card you would like to search for')
        print(search_cards(name))
    elif choice == 3:
        name = str_check('What is the name of the card you would like to remove')
        print(remove_card(name))
    elif choice == 4:4
        print(return_cards())
    else:
        print('Goodbye!')
        sys.exit()
        
def main():
    '''welome message converted to easygui'''
    choice = eg.buttonbox('Welcome to Monster Cards Catalogue'
                          'What would you like to do?', 'Welcome',
                          ('Add card', 'Remove card', 'Search for card', 'Print cards', 'Exit'))
    if choice == 'Add card':
        name = eg.enterbox('What is the name of the card you would like to add?')
        add_card(name)
        
if __name__ == "__main__":
    main()