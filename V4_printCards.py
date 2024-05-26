'''V2_printCards.py
returns card details form txt file, adds easyGUI functionlity'''
import shelve
import easygui as eg

def return_cards():
    '''returns card data from text file'''
    d = shelve.open('cards.txt')
    data = d['cards']
    d.close()
    print(data)
    msg = ""
    for name, stats in data.items():
        msg += f"-- {name.capitalize()} --\nStrength: {stats[0]}\n"
        msg += f"Speed: {stats[1]}\nStealth: {stats[2]}\nCunning: {stats[3]}\n\n"
    msg += '-' * 15
    print(msg)
    msg += "\nCards also outputted to the console"
    eg.msgbox(msg, "Card catalogue")
