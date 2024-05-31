"""V4_addCards.py
adds error checking"""
import shelve
import easygui as eg


def add_card(name):
    """added GUI functionality to adding cards"""
    d = shelve.open('cards.txt')
    data = d['cards']
    try:
        if name in data:
            eg.msgbox(f'The card "{name.capitalize()}" already exists', 'Cancelled add card')
            return
        stats = []
        key = ['strength', 'speed', 'stealth', 'cunning']
        for i in range(4):
            while True:
                stat = eg.integerbox(f'Enter {key[i]} (1-25):', 'Add card', None, 1, 25)
                if stat is None:
                    eg.msgbox("Operation cancelled", "Add card")
                    return
                break
            stats.append(stat)

        if eg.ynbox(f'Are all the details correct?\n\n---{name}---\nStrength: {stats[0]}\n'
                    f'Speed: {stats[1]}\nStealth: {stats[2]}\nCunning: {stats[3]}', 'Add card'):
            data[name] = stats
            d['cards'] = data
            d.close()
            eg.msgbox('Card added!', 'Add card')
        else:
            choice = eg.ynbox('Would you like to try again?', 'Add card')
            if choice:
                name = eg.enterbox('What is the name of the card you would like to add?',
                                   'Add card')
                add_card(name)
            else:
                return
    except TypeError:
        return
