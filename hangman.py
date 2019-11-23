# -*- coding: utf-8 -*-

"""
Hangman The Game
Author: rcmonteiro
Date:   2019-11-22
"""

# Import libs
import random as rd
from os import system


# The Hangman Class
class Hangman(object):

    # Constructor
    def __init__(self):

        # Empty game state
        self.word = ""
        self.wordMatches = []
        self.errors = 0
        self.win = False

        # Get the word for the current game
        with open('files/words.txt', 'r') as file:
            word = rd.choice(file.read().split('\n'))

            for i in word:
                if i == " ":
                    self.wordMatches.append([i, " "])
                else:
                    self.wordMatches.append([i, "_"])

            self.word = word.replace(" ", "").lower()

        # Render the board
        self.renderBoard()

        # Loop until WIN or LOSE
        while True:
            # Ask a guess
            self.guess()

            # WIN or LOSE exit loop
            if self.errors >= 6 or self.win:
                break

    # Ask a guess method
    def guess(self):
        currentGuess = str(input('Type a letter: '))[0:1].lower()

        if self.word.count(currentGuess) > 0:
            self.guessMatch(currentGuess)
        else:
            self.guessError()

    # Compute errors
    def guessError(self):
        self.errors += 1
        self.renderBoard()

    # Compute matches
    def guessMatch(self, letter):
        missing = 0

        for i, val in enumerate(self.wordMatches):

            if self.wordMatches[i][0].lower() == letter:
                self.wordMatches[i][1] = self.wordMatches[i][0]

            if self.wordMatches[i][1] == "_":
                missing += 1

        if missing == 0:
            self.win = True

        self.renderBoard()

    # Render board method
    def renderBoard(self):

        # Clear prompt
        system('clear')

        board = "HANGMAN THE GAME\n"
        board += "--------------------\n"
        board += "Type Ctrl^C to Exit\n"
        board += "--------------------\n\n"

        if self.win:
            board += open('files/victory.txt', 'r').read()
            board += '\n\n'

        if self.errors >= 6:
            board += open('files/gameover.txt', 'r').read()
            board += '\n\n'

        board += open('files/error_%d.txt' % self.errors, 'r').read()
        board += '\n\n'
        for i, val in enumerate(self.wordMatches):
            board += " "
            board += self.wordMatches[i][1]

        print("\n\n\n", board, "\n\n")


# Instance of Hangman
game = Hangman()
