'''dictonary of cards, resets dictionary to original'''
import shelve

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
            'wispgoul': [17, 19, 3, 2]}
    d['cards'] = data
    d.close()
