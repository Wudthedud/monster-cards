'''V1_updateCards.py
saves card details in a persistent text file'''
import shelve

def updateCards(name, stats):
    '''updates text file with card data'''
    d = shelve.open('cards.txt')
    data = d['cards']
    data[name] = stats
    d['cards'] = data
    d.close()

def returnCards():
    '''returns card data from text file'''
    d = shelve.open('cards.txt')
    data = d['cards']
    d.close()
    for name, stats in data.items():
        print(f"{name}, {stats}\n")
returnCards()