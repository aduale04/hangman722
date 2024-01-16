Hangman Game
Hangman is a classic word guessing game. This project implements a simple version of Hangman in Python. The player tries to guess the word by suggesting letters within a certain number of guesses.

Features
Random word selection from a predefined list.
The player is allowed a fixed number of incorrect guesses.
Repeated letters in words are handled correctly.
The game tracks and displays guessed letters and remaining lives.
Requirements
Python 3.x
How to Play
Clone/download the repository to your local machine.
Run the Python script in a terminal or an IDE.
The game will randomly select a word and display a series
of underscores representing each letter in the word.
4. Type in your guess (a single letter) and press Enter.

If your guess is in the word, the letter will be revealed in its correct positions.
If your guess is incorrect, you lose one life.
The game continues until you either guess the word correctly or run out of lives.
If you guess the word correctly, you win! If you run out of lives, the game will reveal the word and end.
Sample Word List
The default word list includes:

apple
strawberry
peach
orange
watermelon
You can modify the word list in the script to include more words or different categories.

Customization
num_lives: Change the number of lives (guesses) allowed (default is 5).
word_list: Modify this list to include words of your choice.
Running the Game
To run the game, navigate to the folder containing the script and run the following command:
python hangman.py
