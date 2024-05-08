'''V2_printCards.py
returns card details form txt file'''

import shelve

def return_cards():
    '''returns card data from text file'''
    d = shelve.open('cards.txt')
    data = d['cards']
    d.close()
    print(data)
    
    for name, stats in data.items():
        print(f"-- {name.capitalize()} --")
        print(f"Strength: {stats[0]}
              f"Speed: {stats[1]})
return_cards()
