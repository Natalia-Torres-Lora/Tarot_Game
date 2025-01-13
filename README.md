# Tarot_Game
Python Fundamentals course final Project

Tarot Game
1. Welcome the user and ask for their question or area of focus.
2. input from user
3. Simulate shuffling a virtual Tarot deck, output a deck of cards.
4. Ask user to draw 3 number of cards from the deck.
5. computer would select random of thre object carts
6. Interpret the meaning of each card based on its position (Past, Present Future).
7. Combine the interpretations for the cards .
8. Display the reading to the user.
9. option to repeat the reading, ask another question or exit the game.


Your Report

* In a word processing application of your choice (such as MS Word or Google Docs), write a report that answers the following questions:

1. What game have you decided for your portfolio project? If you're having a hard time choosing, choose an open-ended game such as a text adventure/choose-your-own-adventure, or one of the other examples given in Week 1.
2. Consider the Python data structures you have learned this week, in relation to your project idea. What are some kinds of data in your project, and what would you guess would be the best way to store that data?
3. Examples:
    * If you have a card game, you might store card values in a list or dictionary.
    * If you have a choose-your-own-adventure game, you might have a list of characters that the player might encounter in the game. 
    * What are the values you might store in a data structure, versus a primitive such as an Integer or Boolean?
4. Based on what you have learned so far, write or rewrite the high-level algorithm for your game. You do not need to use code to write this. You can use pseudocode, or regular English to describe each step of your game. 
5. TIP! If you are looking for more functionality to add to your game, here are some ideas:
        * Keep a high score count, or leaderboard with player names (for the current session since we have not discussed saving data to files; for more advanced Pythonistas, you can try saving the high score/leaderboard to a file). 
        * Set a maximum number of total losses before the game automatically quits. 
        * Add a way for two players at the same computer to play against each other by taking turns at the keyboard.
        * Try to think of other functionality you could add!



Tarot Game 

1. Welcome the user and ask for their question or area of focus.
    input() function to get user input
    print() function to display welcome message
2. Input the user's question.
        Store user input in a variable using question = input()
3. Simulate shuffling the virtual tarot deck.
       Use random.shuffle() function to shuffle the deck
4. Display the deck of cards to the user.
5. Use a for loop to iterate through the deck and print() each card
6. Ask the user to draw a specified number of cards (e.g., 3).
        Use input() function to get user input
        Validate user input using if statements to ensure a valid number is entered
7. Use random selection to choose the specified number of cards from the deck.
8. Use random.sample() function to select a specified number of unique cards from the deck
9. Interpret the meaning of each card based on its position (Past, Present, Future).
          Use a dictionary to store the meanings of each card
          Use if statements to determine the position of each card and retrieve its meaning from the dictionary
10. Combine the interpretations for the cards to provide a reading.
          Use a string variable to store the combined interpretation
            Use += operator to concatenate the interpretations of each card
11. Display the reading to the user.
         Use print() function to display the combined interpretation
12. Provide options for the user to repeat the reading, ask another question, or exit the game.
        Use input() function to get user input
        Use if statements to determine the user's choice and perform the corresponding action


