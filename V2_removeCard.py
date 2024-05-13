'''V2_removeCards.py
removes selected card'''
import shelve

def remove_card(name):
    '''removes card'''
    d = shelve.open('cards.txt')
    data = d['cards']
    
    try:
        del data[name]
        d['cards'] = data
        msg = 'Card removed'
        return msg
    except KeyError:
        msg = 'Card not found'
    d.close()