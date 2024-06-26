'''V2_addCards.py
gets card details and saves them into the text file'''
import shelve

def add_card(name):
    '''updates text file with card data''' 
    stats = []
    strength = int(input("Enter strength (1-25): "))
    speed = int(input("Enter speed (1-25): "))
    stealth = int(input("Enter stealth (1-25): "))
    cunning = int(input("Enter cunning (1-25): "))
    stats.extend([strength, speed, stealth, cunning])

   
    d = shelve.open('cards.txt')
    data = d['cards']
    data[name] = stats
    d['cards'] = data
    d.close()
    print("Card added")
