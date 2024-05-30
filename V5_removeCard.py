'''V4_removeCards.py
removes selected card, adds error checking'''
import shelve
import easygui as eg

def remove_card(name=None):
    '''adds easyGUI to the remove card function'''
    d = shelve.open('cards.txt')
    data = d['cards']

    while True:
        if name is None:
            keys = [key.title() for key in data.keys()]
            name = eg.choicebox("Which card would you like to remove?", "Remove card", keys)
            if name is None:
                eg.msgbox('Operation cancelled', 'Remove card')
                d.close()
                return
        choice = eg.ynbox(f'Are you sure you want to remove "{name.capitalize()}"?', 'Remove card')
        if choice:
            del data[name.lower()]
            d['cards'] = data
            eg.msgbox(f'Card "{name.capitalize()}" removed','Remove card')
            d.close()
            return
        else:
            eg.msgbox('Operation cancelled', 'Remove card')
            return