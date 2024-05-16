'''V2_addCards.py
adds error checking'''
import shelve
from V1_strCheck import card_intcheck


def add_card(name):
    '''updates text file with card data''' 
    stats = []
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
    msg = 'Card added'
    return msg
