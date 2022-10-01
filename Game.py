# Runs the Wordle Game for users and solvers
# James Natoli, 2022

# This will get a random soln from text file
# check the guesses with the soln
# check if the guess is a valid word
# provide feedback on the guess in a usable format
# Ideally, easily allow repetetive plays

import os
import sys
import random
import numpy as np

five_file_name = '/Users/jamesnatoli/Documents/Programs/Wordle/FiveLetterWords.txt'
allWords_file_name = '/Users/jamesnatoli/Documents/Programs/Wordle/AllWords.txt'

class Game:
    def __init__( self, num=5):
        """Initialize object, get the solution"""
        self.solLength = num
        # Get solution
        self.allWords = []
        self.guess = ""
        self.solution = self.getWords()

        # Remember to delete this
        # print( self.solution)

    def getWords( self):
        """Save all the possible words as a member list"""
        with open(allWords_file_name, 'r') as fi:
                self.allWords = list( map( str.rstrip, list( filter( lambda w: (len(w) == self.solLength+1), fi))))
                if self.allWords == []:
                    raise Exception("No words of length %s :("%( self.solLength))
                else:
                    return np.random.choice( self.allWords)
        
    def nextGuess( self, inGuess):
        """Receive the guess as string, return feedback on it"""
        self.guess = inGuess
        if self.isSolution(): return [2] * self.solLength
        else: return self.checkSolution_temp()

    def isSolution( self):
        """Checks if guess is exactly equal to solution"""
        return (self.guess == self.solution)

    def checkSolution_temp( self):
        feedback = [0] * self.solLength
        
        tempSol = list(self.solution)
        for idx, el in enumerate( self.guess):
            if el == tempSol[idx]: # Green, correct
                feedback[idx] = 2
                tempSol[idx] = '*'
        
        for idx, el in enumerate( self.guess): # Now do Yellows
            if feedback[idx] == 0 and el in tempSol: # in word, wrong spot
                feedback[idx] = 1
                tempSol[ tempSol.index(el)] = '*'

        return feedback
    
    def isValid( self, inGuess):
        """Checks if the guess is a valid word"""
        return inGuess in self.allWords

    def resetGame( self):
        """Set everything to beginning, get a new word"""
        pass
