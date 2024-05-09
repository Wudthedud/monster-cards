'''V1_monsterCards.py
main program that calls other functions'''
import sys
from V1_updateCards import add_card, remove_card, return_cards, search_cards

def welcome():
    '''welcome()
    prints welcome message to user'''
    print('Welcome to monster cards!')
    choice = int(input(
          'What would you like to do?\n'
          '[1] Add card\n[2] Search for Cards\n'
          '[3] Delete Card\n[4] Print all cards\n[5] Exit\n'))

    if choice == 1:
        name = input('What is the name of your card?\n')

        stats = []
        strength = int(input("Enter strength (1-25): "))
        speed = int(input("Enter speed (1-25): "))
        stealth = int(input("Enter stealth (1-25): "))
        cunning = int(input("Enter cunning (1-25): "))
        stats.extend([strength, speed, stealth, cunning])

        add_card(name, stats)
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
