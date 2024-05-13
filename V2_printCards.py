'''V2_printCards.py
returns card details form txt file'''

import shelve

def return_cards():
    '''returns card data from text file'''
    d = shelve.open('cards.txt')
    data = d['cards']
    d.close()
    print(data)
    
    msg = ""
    for name, stats in data.items():
        msg += f"-- {name.capitalize()} --\nStrength: {stats[0]}\n"
        msg += f"Speed: {stats[1]}\nStealth: {stats[2]}\nCunning: {stats[3]}\n\n"
    msg += '-' * 15
    return msg

print(return_cards())