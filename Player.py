# Class to allow a user to play Wordle through the terminal
# It would be cool to get a GUI working for this, using Tkinter or something
# James Natoli, 2022

import os
import sys
import random
import numpy as np
from termcolor import colored, cprint

from Letter import Letter
from Game import Game

class Player:
    def __init__( self):
        """Initialize object"""
        self.currentGame = Game()

        # array of Letter objects
        self.guess = []
        for i in range( 0, 5):
            self.guess.append( Letter( '', i))

    def runGame( self):
        """Start the game"""
        for turn in range(1, 6):
            inguess = input('Guess %d/6: \t'%(turn))
            self.incorporateFeedback( self.currentGame.nextGuess( inguess))

    def incorporateFeedback( self, feedback):
        """Update the 'guess' array with the Game feedback"""
        for i in range( 0, len(feedback)):
            self.guess[i].setColor( feedback[i])
        self.printGuess()

    def printGuess( self):
        coloredText = colored('')
        text = ''
        for el in self.guess:
            coloredText = text + colored( self.padText( el.getText()), 'white', el.getColor())
        return coloredText
                                
    def padText( self, someText):
        return ' ' + someText + ''
    
