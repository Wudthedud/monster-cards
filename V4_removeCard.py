'''V4_removeCards.py
removes selected card, adds error checking'''
import shelve
import easygui as eg

def remove_card(name):
    '''adds easyGUI to the remove card function'''
    d = shelve.open('cards.txt')
    data = d['cards']
    try:
        if name in data:
            choice = eg.ynbox(f'Are you sure you want to remove {name}?', 'Remove card')
            if choice:
                del data[name]
                d['cards'] = data
                eg.msgbox(f"Card '{name} removed")
            if not choice:
                eg.msgbox('Card deletion cancelled', 'Remove ')
        else:
            choice = eg.ynbox(f'The card "{name}" could not be found, woul dyou like to try again?',
                              'Remove card')
            if choice:
                name = eg.enterbox('What is the name of the card you would like to add?')
                remove_card(name)
            else:
                return
    except KeyError:
        eg.msgbox(f'The card {name} could not be found')
        return
    except TypeError:
        eg.msgbox('Card removal cancelled')
        return
