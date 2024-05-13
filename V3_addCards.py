'''V2_addCards.py
gets card details and saves them into the text file'''
import shelve
from V1_strCheck import str_check, card_intcheck


def add_card():
    '''updates text file with card data''' 
    stats = []
    name = str_check("Enter the name of the new card")
    strength = card_intcheck("Enter strength (1-25)")
    strength = card_intcheck("Enter strength (1-25): ")
    speed = card_intcheck("Enter speed (1-25): ")
    stealth = card_intcheck("Enter stealth (1-25): ")
    cunning = card_intcheck("Enter cunning (1-25): ")
    stats.extend([strength, speed, stealth, cunning])

    d = shelve.open('cards.txt')
    data = d['cards']
    data[name] = stats
    d['cards'] = data
    d.close()
    print("Card added")

add_card()
