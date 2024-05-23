'''V4_removeCards.py
removes selected card, adds error checking'''
import shelve
import easygui as eg
from V4_monsterCards import main

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
        return msg
    d.close()

def remove(name):
    '''adds easyGUI to the remove card function'''
    d = shelve.open('cards.txt')
    data = d['cards']
    try:
        if name in data:
            choice = eg.ynbox(f'Are you sure you want to remove {name}?', 'Remove card')
            if choice:
                del data[name]
                d['cards'] = data
                eg.msgbox(f"{name} card removed")
            if not choice:
                eg.msgbox('Card deletion cancelled', 'Remove ')
                main()
    except KeyError:
        eg.msgbox(f'The card {name} could not be found')
        main()
    except TypeError:
        main()
