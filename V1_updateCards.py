'''V1_updateCards.py
saves card details in a persistent text file'''
import shelve

def add_card(name, stats):
    '''updates text file with card data'''
    d = shelve.open('cards.txt')
    data = d['cards']
    data[name] = stats
    d['cards'] = data
    d.close()

def remove_card(name):
    '''removes card'''
    d = shelve.open('cards.txt')
    data = d['cards']
    del data[name]
    d['cards'] = data
    d.close()
    
def return_cards():
    '''returns card data from text file'''
    d = shelve.open('cards.txt')
    data = d['cards']
    d.close()
    print(data)

card_name = input("Enter new card name: ")
card_stats = input("Enter stats: ")
stats_list = list(map(int, str(card_stats[0])))
add_card(card_name, stats_list)
return_cards()
