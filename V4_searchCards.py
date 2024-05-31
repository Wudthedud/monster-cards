'''V4_search_cards.py
saerches for a card and returns it's details'''
import shelve
import easygui as eg
from V5_removeCard import remove_card

def search_card(name):
    """searches for card within the dictionaryx"""
    d = shelve.open('cards.txt')
    data = d['cards']
    d.close()
    while True:
        keys = [key.title() for key in data.keys()]
        name = eg.choicebox("Which card would you like to remove?", "Remove card", keys)
        if name is None:
            eg.msgbox('Operation cancelled', 'Remove card')
            return
        while True:
            stats = data.get(name)
            choice = eg.buttonbox(f'Card found:\n\n---{name.capitalize()}---\nStrength: {stats[0]}'
                                  f'\nSpeed: {stats[1]}\nStealth: {stats[2]}\nCunning: {stats[3]}'
                                  '\n\nWhat would you like to do?', 'Search for a card', 
                    ["Edit card", "Remove Card", "Go back"])
            if choice == "Edit card":
                choice2 = eg.buttonbox("What would you like to edit", "Edit a card",
                                    ["Edit name", "Edit stats", "Go back"])
                if choice2 == "Edit name":
                    edit_name(name)
                elif choice2 == "Edit stats":
                    edit_stats(name)
            elif choice == "Remove Card":
                remove_card(name)
            elif choice == "Go back":
                return
            else:
                choice = eg.ynbox(f'The card "{name}" could not be found,'
                                  f'would you like to try again?', 'Search for a card')
                if choice:
                    name = eg.enterbox('What is the name of the card you would like to search for?')
                    if name is not None:
                        search_card(name)
                    else:
                        eg.msgbox("Operation cancelled", "Search for card")
                        return

def edit_name(name):
    """edits a key within a dictionary"""
    d = shelve.open('cards.txt')
    data = d['cards']
    stats = data.get(name)
    while True:
        new_name = eg.enterbox('What would you like to rename the card to?')
        if new_name is None:
            eg.msgbox("Operation cancelled")
            search_card(name)
        elif new_name == "":
            eg.msgbox("This field cannot be empty", "Edit card")
        else:
            confirm = eg.ynbox(f"Here is your new card:"
                                f"\n\n---{new_name.capitalize()}---\nStrength: {stats[0]}\n"
                                f"Speed: {stats[1]}\nStealth: {stats[2]}\n"
                                f"Cunning: {stats[3]}\n\n","Confirm?", "Edit card")
            if confirm:
                data[new_name] = data.pop[name]
                eg.msgbox("Operation completed", "Edit card")
                d['cards'] = data
                d.close()
            else:
                eg.msgbox("Operation cancelled", "Edit card")
                search_card(name)

def edit_stats(name):
    """edits a key within a dictionary"""
    d = shelve.open('cards.txt')
    data = d['cards']
    stats = data.get(name)
    while True:
        choice = eg.buttonbox("Which statistic would you like to edit?\n\n"
                                f"---{name.capitalize()}---\nStrength: {stats[0]}\n"
                                f"Speed: {stats[1]}\nStealth: {stats[2]}\n"
                                f"Cunning: {stats[3]}\n\n", "Edit card",
                                ['Strength', 'Speed', 'Stealth', 'Cunning', 'Cancel'])
        if choice in ['Strength', 'Stealth', 'Speed', 'Cunning']:
            new_stat = eg.integerbox('What would you like to rename the card to?')
            if new_stat is None:
                eg.msgbox("Operation cancelled")
                search_card(name)
            elif new_stat == "":
                eg.msgbox("This field cannot be empty", "Edit card")
            key = {'Strength': 0, 'Speed': 1, 'Stealth': 2, 'Cunning': 3}
            stats[key[choice]] = new_stat
            confirm = eg.ynbox(f"Here is your new card:"
                                    f"\n\n---{name.capitalize()}---\nStrength: {stats[0]}\n"
                                    f"Speed: {stats[1]}\nStealth: {stats[2]}\n"
                                    f"Cunning: {stats[3]}\n\nConfirm?", "Edit card")
            if confirm:
                data[name] = stats
                eg.msgbox("Operation completed", "Edit card")
                d['cards'] = data
                d.close()
            else:
                eg.msgbox("Operation cancelled")
                search_card(name)
        elif choice == "Cancel":
            search_card(name)
