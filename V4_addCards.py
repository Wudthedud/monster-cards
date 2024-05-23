'''V4_addCards.py
adds error checking'''
import shelve
import easygui as eg


def add_card(name):
    '''added GUI functionality to adding cards'''
    from V4_monsterCards import main
    d = shelve.open('cards.txt')
    data = d['cards']
    try:
        
        if name in data:
            eg.msgbox(f'This card {name} already exists', 'Cancelled add card')
            main()
            return None
        stats = []
        strength = eg.integerbox('Enter strength (1-25):', 'Add card', None, 1, 25)
        
        speed = eg.integerbox('Enter speed (1-25):', 'Add card', None, 1, 25)
        stealth = eg.integerbox('Enter stealth (1-25):', 'Add card', None, 1, 25)
        cunning = eg.integerbox('Enter cunning (1-25):', 'Add card', None, 1, 25)
        stats.extend([strength, speed, stealth, cunning])


        if eg.ynbox(f'Are all the details correct?\n\n---{name}---\nStrength: {strength}\n'
                    f'Speed: {speed}\nStealth: {stealth}\nCunning: {cunning}', 'Add card'):
            data[name] = stats
            d['cards'] = data
            d.close()
            eg.msgbox('Card added!', 'Add card')
        else:
            choice = eg.ynbox('Would you like to try again?', 'Add card')
            if choice:
                name = eg.enterbox('What is the name of the card you would like to add?', 'Add card')
                add_card(name)
            else:
                main()
    except TypeError:
        main()
        