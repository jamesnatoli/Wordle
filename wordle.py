# Fake Wordle
# James Natoli, 2022

import os
import sys
import random
import numpy as np
from termcolor import colored, cprint

from letter import letter

file_name = '/Users/jamesnatoli/Documents/Programs/Wordle/FiveLetterWords.txt'

def getWords( num=6):
    with open(file_name, 'r') as fi:
        return list( map( str.rstrip, list( filter( lambda w: (len(w) == num), fi))))

def check( guess, answer):
    # guess is a list of letter objects
    assert len( guess) == len(answer), 'WORDLE NOT HAPPY'
    cnt = 0
    for le in guess:
        te = le.getText()
        if te == answer[cnt]:
            le.setColor( 'green')
        elif (te in answer):
            le.setColor( 'yellow')
        else:
            le.setColor( 'red')
        cnt = cnt + 1

    return guess
    
def main():
    print("Welcome to Wordle!")
    print(" _ _ _ _ _ ")
    answer = np.random.choice( getWords())
    # answer = 'fruit'
    # print(f'Answer: {answer}')
    
    text = colored('Hello, World!', 'red', attrs=['blink'])
    cprint('whoops', 'green', 'on_blue', attrs=['underline'])
    print(text)

    print(colored('this is red', 'red'))
    print(colored('this is yellow', 'yellow'))
    print(colored('this is green', 'green'))

    guess = []
    inguess = input('Guess 1/6: \t')

    assert len( inguess) == 5, 'WORDLE NOT HAPPY'
    
    for i in range( 0, len(inguess)):
        guess.append( letter( inguess[i], i))
    checkedGuess = check( guess, answer)
    for i in checkedGuess:
        cprint( i.getText(), i.getColor())
    
    for i in range(0, 4):
        guess = []
        inguess = input("Guess %d/6: \t"%(i+2))
        assert len( inguess) == 5, 'WORDLE NOT HAPPY'
        
        for i in range( 0, len(inguess)):
            guess.append( letter( inguess[i], i))
            
        checkedGuess = check( guess, answer)
        
        for i in checkedGuess:
            cprint( i.getText(), i.getColor())

        if inguess == answer:
            print('You\'ve got it!')
            break

    print("Answer was: %s"%( answer))

if __name__ == "__main__":
    main()
