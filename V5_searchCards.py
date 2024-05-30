'''V4_search_cards.py
saerches for a card and returns it's details'''
import shelve
import easygui as eg
from V5_removeCard import remove_card

def search_card(name=None):
    '''searches for card within the dictionary'''
    while True:
        d = shelve.open('cards.txt')
        data = d['cards']
        d.close
        if name is None:
            keys = [key.title() for key in data.keys()]
            name = eg.choicebox('Which card would you like to search for?', 'Search/Edit card',
                                keys)
            if name is None:
                eg.msgbox('Operation cancelled', 'Remove card')
                return
        
        name = name.lower()
        stats = data.get(name)
        print(name, stats)
        choice = eg.buttonbox(f'Card found:\n\n---{name.capitalize()}---\nStrength: {stats[0]}'
                                f'\nSpeed: {stats[1]}\nStealth: {stats[2]}\nCunning: {stats[3]}\n'
                                f'\nWhat would you like to do?', 'Search for a card',
                                ['Edit card', 'Remove Card', 'Go back'])
        if choice == 'Edit card':
            choice2 = eg.buttonbox('What would you like to edit', 'Edit a card',
                                ['Edit name', 'Edit stats', 'Go back'])
            if choice2 == 'Edit name':
                name = edit_name(name)
            elif choice2 == 'Edit stats':
                edit_stats(name)
            else:
                return
        elif choice == 'Remove Card':
            remove_card(name)
            return
        else:
            return


def edit_name(name):
    '''edits a key within a dictionary'''
    d = shelve.open('cards.txt')
    data = d['cards']
    stats = data.get(name)
    while True:
        new_name = eg.enterbox('What would you like to rename the card to?', 'Edit card').lower()
        if new_name is None:
            eg.msgbox('Operation cancelled', 'Edit card')
            return
        elif new_name == '':
            eg.msgbox('This field cannot be empty', 'Edit card')
        elif new_name in data:
            eg.msgbox(f'The card "{name.capitalize()}" already exists', 'Cancelled add card')
        else:
            confirm = eg.ynbox(f'Here is your edited card:'
                                f'\n\n---{new_name.capitalize()}---\nStrength: {stats[0]}\n'
                                f'Speed: {stats[1]}\nStealth: {stats[2]}\n'
                                f'Cunning: {stats[3]}\n\nConfirm?', 'Edit card')
            if confirm:
                data[new_name] = data.pop(name)
                d['cards'] = data
                d.close()
                eg.msgbox('Operation complete', 'Edit card')
                return new_name
            else:
                eg.msgbox('Operation cancelled', 'Edit card')
                return

def edit_stats(name): #TODO button for strength
    '''edits a key within a dictionary'''
    d = shelve.open('cards.txt')
    data = d['cards']
    stats = data.get(name)
    while True:
        choice = eg.buttonbox('Which statistic would you like to edit?\n\n'
                                f'---{name.capitalize()}---\nStrength: {stats[0]}\n'
                                f'Speed: {stats[1]}\nStealth: {stats[2]}\n'
                                f'Cunning: {stats[3]}\n\n', 'Edit card',
                                ['Strength', 'Stealth', 'Speed', 'Cunning', 'Cancel'])
        if choice in ['Strength', 'Stealth', 'Speed', 'Cunning']:
            new_stat = eg.integerbox(f'What would you like to change the {choice} to?')
            if new_stat is None:
                eg.msgbox('Operation cancelled')
                search_card(name)
            elif new_stat == '':
                eg.msgbox('This field cannot be empty', 'Edit card')
            key = {'Strength': 0, 'Stealth': 1, 'Speed': 2, 'Cunning': 3}
            stats[key[choice]] = new_stat
            confirm = eg.ynbox(f'Here is your new card:'
                                    f'\n\n---{name.capitalize()}---\nStrength: {stats[0]}\n'
                                    f'Speed: {stats[1]}\nStealth: {stats[2]}\n'
                                    f'Cunning: {stats[3]}\n\n','Confirm?', 'Edit card')
            if confirm:
                data[name] = stats
                eg.msgbox('Operation completed', 'Edit card')
                d['cards'] = data
                d.close()
            else:
                eg.msgbox('Operation cancelled')
                search_card(name)
        elif choice == 'Cancel':
            search_card(name)
