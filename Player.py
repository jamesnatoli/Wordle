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
        self.isSolved = False

        # array of Letter objects
        self.guess = []
        for i in range( 0, 5):
            self.guess.append( Letter( '', i))

    def runGame( self):
        """Start the game"""
        for turn in range(1, 6):
            if self.isSolved:
                print("Great work!! :)")
                break
            inGuess = input('Guess %d/6: \t'%(turn))
            assert len( inGuess) == 5, 'Please input a word of correct length...'
            for i in range( 0, 5):
                self.guess[i].setText( inGuess[i])
            self.incorporateFeedback( self.currentGame.nextGuess( inGuess))

    def incorporateFeedback( self, feedback):
        """Update the 'guess' array with the Game feedback"""
        if feedback == [ 2, 2, 2, 2, 2]:
            self.isSolved = True
        for i in range( 0, len(feedback)):
            self.guess[i].setColor( feedback[i])
            
        self.printGuess()
        
    def printGuess( self):
        print( ''.join( [str(el) for el in self.guess]))
                                
    def padText( self, someText):
        return ' ' + someText + ''
    
