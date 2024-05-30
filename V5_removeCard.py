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
        choice = eg.ynbox(f'Are you sure you want to remove "{name}"?', 'Remove card')
        if choice:
            del data[name.lower()]
            d['cards'] = data
            try_again = eg.ynbox(f'Card "{name}" removed, do you want to remove another card?',
                                 'Remove card')
            if try_again:
                name = None
            else:
                d.close()
                return
        else:
            try_again = eg.ynbox('Operation cancelled, would you like to try again?', 'Remove card')
            if try_again:
                name = None
            else:
                d.close()
                return
