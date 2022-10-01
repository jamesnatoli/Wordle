# Runs the Wordle Game for users and solvers
# James Natoli, 2022

# This will get a random soln from text file
# check the guesses with the soln
# check if the guess is a valid word
# provide feedback on the guess in a usable format
# Ideally, easily allow repetetive plays

# Important rules
# correct gets a 2
# incorrect gets a 0
# wrong spot gets a 1
# feedback about a letter is only given once
# meaning, if you guess a duplicate letter, only one will have info
# if one is in the correct spot, give info about that
# otherwise, just the first occurrance

import os
import sys
import random
import numpy as np

five_file_name = '/Users/jamesnatoli/Documents/Programs/Wordle/FiveLetterWords.txt'
all_file_name = '/Users/jamesnatoli/Documents/Programs/Wordle/AllWords.txt'

class Game:
    def __init__( self, num=5):
        """Initialize object, get the solution"""
        self.solLength = num
        # Get solution
        self.allWords = []
        self.guess = ""
        self.remainingGuesses = 6
        self.duplicates = {}
        self.solution = self.getWords()

        # Remember to delete this
        print( self.solution)

    def getWords( self):
        """Save all the possible words as a member list"""
        if self.solLength != 5:
            print("not working yet...")
            exit(0)
            with open(allWords_file_name, 'r') as fi:
                # return np.random.choice( np.array( map( str.rstrip, list( filter( lambda w: (len(w) == self.solLength), fi)))))
                self.allWords = list( map( str.rstrip, list( filter( lambda w: (len(w) == self.solLength+1), fi))))
                return np.random.choice( self.allWords)
        else:
            with open(five_file_name, 'r') as fi:
                self.allWords = list( map( str.rstrip, fi.readlines()))
                return np.random.choice( self.allWords)
        
    def nextGuess( self, inGuess):
        """Receive the guess as string, return feedback on it"""
        assert self.isValid( inGuess), 'Please input a valid word...'
        self.guess = inGuess
        if self.isSolution():
            return [ 2, 2, 2, 2, 2]
        else:
            if self.guessDuplicates() and not self.solutionDuplicates():
                # print ("no duplicates please, not working yet...")
                # exit(0)
                return self.checkDupSolution()
            else:
                return self.checkSolution()

    def isSolution( self):
        """Checks if guess is exactly equal to solution"""
        return (self.guess == self.solution)

    def checkSolution( self):
        """Provides feedback about individual letters"""
        feedback = [ 99, 99, 99, 99, 99]
        checked = []
        count = 0
        for el in self.guess:
            if el == self.solution[count]: # Green, correct
                feedback[count] = 2
            elif (el not in self.solution): # Grey, not in word
                feedback[count] = 0
            else: # Yellow, in word, wrong spot
                feedback[count] = 1
            count = count + 1
        return feedback

    def solutionDuplicates( self):
        """Duplicates in solution"""
        checked = []
        dupFlag = False
        for el in self.solution:
            if el in checked:
                dupFlag = True
                checked.append( el)
            else:
                checked.append( el)
        return dupFlag

    def guessDuplicates( self):
        """Checks if there are duplicate letters in the guess"""
        checked = []
        dupFlag = False
        for el in self.guess:
            if el in checked:
                dupFlag = True
                self.duplicates[el] = []
                checked.append( el)
            else:
                checked.append( el)
        return dupFlag

    def dupIndex( self):
        """Adds the positions of the duplicate letters to the dictionary"""
        for dupLetter in self.duplicates.keys():
            for idx, el in enumerate( self.guess):
                if dupLetter == el:
                    self.duplicates[dupLetter].append( idx)

    # Consider cases...
    # 1) duplicate set in guess, soln has none
    # - provide the "best" info
    # 2) no duplicates in guess, soln has one
    # - do nothing different
    # 3) duplicates in both
    # - do nothing different??
    # This isn't entirely correct... if guess has 3 of the same and soln only has two of the same it's buggy
    # This seems rare... I will ignore for now
    def checkDupSolution( self):
        """Provides feedback about letters in the event the guess has duplicates, but soln does not"""
        # start with a dictionary of the duplicate letters mapped to their locations
        # consider changing the letter in guess to like '?' or something, this will let you know that it's already been fed back info
        self.dupIndex()
        checked = []
        count = 0
        infoGiven = {}
        for el in self.duplicates.keys():
            infoGiven[el] = False

        # Get info about the non duplicates, then reset the info for the duplicates
        feedback = self.checkSolution()
        for key in self.duplicates:
            for index in self.duplicates[key]:
                feedback[index] = 0
            
        # first check if correct spot
        for el in self.duplicates.keys():
            for index in self.duplicates[el]:
                if el == self.solution[index]:
                    feedback[count] = 2
                    infoGiven[el] = True

        # Only if none were correct, consider setting them yellow
        for el in self.duplicates.keys():
            if not infoGiven[el]:
                for index in self.duplicates[el]:
                    if el in self.solution:
                        feedback[index] = 1
                        infoGiven[el] = True

        return feedback

    def isValid( self, inGuess):
        """Checks if the guess is a valid word"""
        return inGuess in self.allWords

    def resetGame( self):
        """Set everything to beginning, get a new word"""

    def provideFeedback( self):
        """Return information about the guess in a useful way"""
        # what's the best way to do this?
        # simple would be an 5 component array, with 0, 1, 2?
        
# assert len( guess) == len(answer), 'WORDLE NOT HAPPY'
# cnt = 0
# for le in guess:
#     te = le.getText()
#     if te == answer[cnt]:
#         le.setColor( 'green')
#     elif (te in answer):
#         le.setColor( 'yellow')
#     else:
#         le.setColor( 'red')
#     cnt = cnt + 1
