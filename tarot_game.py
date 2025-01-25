#tarot_game.py

from game_pkg.card_class import Card, create_deck, shuffle_deck, draw_3cards
from game_pkg.card_data import cards_data
from game_pkg.ascll_art import start_greeting


# starting the game with a greeting
start_greeting()
print('''
        Welcome to your Tarot Reading! 
        This is your opportunity to dive deep into your past, present, and future, and confidently shape your destiny. Let\'s get started!
      ''')

# Providing an option to the user to choose the type of reading they want
while True:
    option = input('''
Step into the realm of insight and mystery. What truth do you seek to uncover?

            1. Matters of the Heart (Love)
            2. Pathways to Success (Career)
            3. Wellness of Mind and Body (Health)
            4. Fortune and Prosperity (Wealth)
            5. The Unfolding Journey (General Reading)
        
Choose the number that calls to your soul." ''') 

# Mapping the user's choice to the corresponding reading
    if option == '1':
        option = 'Love'
        break
    elif option == '2':
        option = 'Career'
        break
    elif option == '3':
        option = 'Health'
        break
    elif option == '4':
        option = 'Wealth'
        break
    elif option == '5':
        option = 'Unfolding Journey'
        break
    else:
        print('Invalid input. Please choose a number from 1 to 5.')
    
print(f'\nYou have chosen to explore the realm of {option}. Let\'s begin your reading!')

# Initiating the the card reading spread
input('\nFocus your mind and form your question in the realm of the truth you chose. \nWhen ready, press Enter to reveal your cards:')

# Creating the deck of cards
deck = create_deck(option)

# Shuffling the deck
deck = shuffle_deck(deck)

# Drawing 3 cards from the deck
cards = draw_3cards(deck)

# Displaying the cards drawn
print('\nYour cards have been revealed! Here is your reading: \n')
print('Yor Past: ', cards[0].name), print(cards[0].description)
print('\nYour Present: ', cards[1].name), print(cards[1].description)
print('\nYour Future: ', cards[2].name), print(cards[2].description)

print('\nThank you for your trust in the cards. May the wisdom you have gained guide you on your journey.')



