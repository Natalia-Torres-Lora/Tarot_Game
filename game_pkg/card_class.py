# card_class.py
import random

from .card_data import cards_data


class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
def create_deck(option):
    deck = []
    for card, descriptions in cards_data.items():
        deck.append(Card(card, descriptions[option]))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def draw_3cards(deck):
    return deck[:3]
        
