#tarot_game.py
# from game_pkg.card_class import 
# from game_pkg.card_data import
from game_pkg.ascll_art import start_greeting


# starting the game with a greeting
start_greeting()
print('''
        Welcome to your Tarot Reading! 
        This is your opportunity to dive deep into your past, present, and future, and confidently shape your destiny. Let\'s get started!
      ''')

# Providing an option to the user to choose the type of reading they want
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
elif option == '2':
    option = 'Career'
elif option == '3':
    option = 'Health'
elif option == '4':
    option = 'Wealth'
elif option == '5':
    option = 'Unfolding Journey'
else:
    print('Invalid input. Please choose a number from 1 to 5.')
    
print(f'\nYou have chosen to explore the realm of {option}. Let\'s begin your reading!')

# Initiating the thre card reading spread
input('\nFocus your mind and form your question in the realm of the truth you chose. \nWhen ready, press Enter to reveal your cards:')

