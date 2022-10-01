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
    def __init__( self, wordLength):
        """Initialize object"""
        self.isSolved = False
        self.wLength = wordLength
        self.solvedArray = [2] * wordLength
        self.currentGame = Game( self.wLength)

        # will be array of Letter objects
        self.guess = []
        for i in range( 0, self.wLength):
            self.guess.append( Letter( '', i))

    def runGame( self):
        """Start the game and proceed through guesses"""
        print('Welcome to ' + colored(' W ', 'white', 'on_grey') + colored(' O ', 'white', 'on_yellow') + colored(' R ', 'white', 'on_green') +
           colored(' D ', 'white', 'on_grey') + colored(' L ', 'white', 'on_yellow') + colored(' E ', 'white', 'on_green'))
        for turn in range(1, 7): # keep guesses at 6?
            inGuess = input('Guess %d/6: \t'%(turn))
            while not self.currentGame.isValid( inGuess) or not len( inGuess) == self.wLength:
                print( "Please input a valid word...")
                inGuess = input('Guess %d/6: \t'%(turn))
            for i in range( 0, self.wLength):
                self.guess[i].setText( inGuess[i])
            self.incorporateFeedback( self.currentGame.nextGuess( inGuess))
            if self.isSolved:
                print("Great work!! :)")
                print("You solved Wordle in %d guesses"%(turn))
                break

        print("Better luck next time... the word was %s"%(self.currentGame.getSolution()))

    def incorporateFeedback( self, feedback):
        """Update the 'guess' array with the Game feedback"""
        if feedback == self.solvedArray:
            self.isSolved = True
        for i in range( 0, len(feedback)):
            self.guess[i].setColor( feedback[i])
            
        self.printGuess()
        
    def printGuess( self):
        print( ''.join( [str(el) for el in self.guess]))
                                
    def padText( self, someText):
        return ' ' + someText + ''
    
