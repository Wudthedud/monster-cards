'''V2_saerchCards.py
saerches for a card and returns it's details'''
import shelve

def search_cards(name):
    d = shelve.open('cards.txt')
    data = d['cards']
    d.close
    if name in data.keys():
        stats = data.get(name)
        msg = ""
        msg += f"-- {name.capitalize()} --\nStrength: {stats[0]}\n"
        msg += f"Speed: {stats[1]}\nStealth: {stats[2]}\nCunning: {stats[3]}\n"
        msg += '-' * 15
        return msg
    else:
        print("Card not found")