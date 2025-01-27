# Tarot Game

##Tarot Card Game
By Natalia Torres Lora

#Introduction 
I developed a basic tarot reading application in which users select a question and draw three cards from a shuffled deck. Each card corresponds to an interpretation of the past, present, and future, providing coherent insights based on the readings derived from the drawn cards.

#Design and Implementation
I created a class to include the properties of the card object. The Card class was designed to capture the characteristics of each Tarot card:
•	Name: The title of the card.
•	Description: A brief meaning customized for different reading types ( Love, Health, Wealth, Career and General Reading).
The card data is stored in a dictionary, where the keys are the card names, and the values are descriptions tailored for the various reading types. 
Next, I developed key functions for the application to improve its user interface and overall performance. I added: 
•	create_deck: Generates a deck of cards based on the user's chosen reading type.
•	shuffle_deck:  Randomizes the order of the cards.
•	draw_3cards: Draws three cards representing the past, present, and future.
The game begins with a greeting, prompting the user to select one of five reading types: Love, Career, Health, Wealth, or General. A deck is created, and shuffled, and three cards are drawn. The meanings of these cards are then displayed to the user, followed by a closing message and ASCII art
. 


#Conclusion
This project taught me the importance of modular programming and code reusability. By dividing the code into different modules and classes, I maintained a clean and organized structure, which made debugging and future enhancements easier. Additionally, incorporating user input and creating a dynamic experience deepened my understanding of Python functions, randomization, and object-oriented programming. The game could benefit from improved user interaction or visuals. In the future, I plan to add various types of draw card variations and more data to interpret reading for a more complex algorithm.
