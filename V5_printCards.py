'''V2_printCards.py
returns card details form txt file, adds easyGUI functionlity'''
import shelve
import easygui as eg


def console_print(data):
    """prints formatted cards to console"""
    for name, stats in data.items():
        msg = "\n"
        width = len(name) + 8
        msg += '-' * (width)
        msg += f'\n|   {name}   |\n'
        msg += '-' * (width)
        msg += '\n'   
        key = ['Strength', 'Speed', 'Stealth', 'Cunning']
        for i, (key, stats) in enumerate(zip(key, stats)):
            stats_msg = f'|{key}: {stats}'
            filler = width - len(stats_msg) - 1
            msg += stats_msg
            msg += ' ' * filler
            msg += '|\n'
        msg += '-' * (width)
        print(msg)

def return_cards():
    '''returns card data from text file'''
    d = shelve.open('cards.txt')
    data = d['cards']
    d.close()
    console_print(data)
    msg = ""
    for name, stats in data.items():
        msg += f"-- {name.capitalize()} --\nStrength: {stats[0]}\n"
        msg += f"Speed: {stats[1]}\nStealth: {stats[2]}\nCunning: {stats[3]}\n\n"
    msg += '-' * 15
    msg += "\nCards also outputted to the console"
    eg.msgbox(msg, "Card catalogue")