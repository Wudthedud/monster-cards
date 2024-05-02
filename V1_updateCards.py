'''V1_updateCards.py
saves card details in a persistent text file'''
import shelve

def updateCards(name, stats):
    d = shelve.open('cards')  # here you will save the score variable
    d['highscores_numbers'] = [["Daniel", 100], ["Name2", 90], ["Name3", 80], ["Name4", 70], ["Name5", 60]]
    d.close()