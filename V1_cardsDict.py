'''dictonary of cards'''
import shelve

cards = {'stoneling': [7, 1, 25, 15],
         'vexscream': [1, 6, 21, 19],
         'dawnmirage': [5, 15, 18, 22],
         'blazegolem': [15, 20, 23, 6],
         'websnake': [7, 15, 10, 5],
         'moldvine': [21, 18, 14, 5],
         'vortexwing': [19, 13, 19, 2],
         'rotthing': [16, 7, 4, 12],
         'froststep': [14, 14, 17, 4],
         'wispgoul': [17, 19, 3, 2]}

cards = {'stoneling': {'strength': 7,
                       'speed': 1,
                       'stealth:': 25,
                       'cunning': 15},
         'vexscream': {'strength': 1,
                       'speed': 6,
                       'stealth:': 21,
                       'cunning': 19},
         'dawnmirage': {'strength': 5,
                       'speed': 15,
                       'stealth:': 18,
                       'cunning': 22},
         'blazegolem': {'strength': 15,
                       'speed': 20,
                       'stealth:': 23,
                       'cunning': 6},
         'websnake': {'strength': 7,
                       'speed': 15,
                       'stealth:': 10,
                       'cunning': 5},
         'moldvine': {'strength': 21,
                       'speed': 18,
                       'stealth:': 14,
                       'cunning': 5},
         'vortexwing': {'strength': 19,
                       'speed': 13,
                       'stealth:': 19,
                       'cunning': 2},
         'rotthing': {'strength': 16,
                       'speed': 7,
                       'stealth:': 4,
                       'cunning': 12},
         'froststep': {'strength': 14,
                       'speed': 14,
                       'stealth:': 17,
                       'cunning': 4},
         'wispgoul': {'strength': 17,
                       'speed': 19,
                       'stealth:': 3,
                       'cunning': 2}}


def reset():
    '''updates text file with card data'''
    d = shelve.open('cards.txt')
    data = {'stoneling': [7, 1, 25, 15],
            'vexscream': [1, 6, 21, 19],
            'dawnmirage': [5, 15, 18, 22],
            'blazegolem': [15, 20, 23, 6],
            'websnake': [7, 15, 10, 5],
            'moldvine': [21, 18, 14, 5],
            'vortexwing': [19, 13, 19, 2],
            'rotthing': [16, 7, 4, 12],
            'froststep': [14, 14, 17, 4],
            'wispgoul': [17, 19, 3, 2],
            'test': [1, 1, 1, 1],
            'ad': [0],
            'adsasd': [1, 1, 1, 1]}
    d['cards'] = data
    d.close()
    
reset()

