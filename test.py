# Driver for Wordle Game
# James Natoli, 2022

from optparse import OptionParser
from termcolor import colored, cprint

# Local Classes
# from Game import Game
from Player import Player
from Letter import Letter

parser = OptionParser()
parser.add_option('--player', '-p', action='store_true', dest='player', 
                  help='Choose this option if you want to play as a Player')
parser.add_option('--solver', '-s', action='store_true', dest='solver',
                  help='Choose this option if you want to watch the Solver')
parser.add_option('--compete', '-c', action='store_true', dest='compete',
                  help='Choose this option if you want to compete with the Solver')
(ops, args) = parser.parse_args()

if ops.__dict__['player'] is not None and (ops.__dict__['solver'] is not None or ops.__dict__['compete'] is not None):
    parser.error('Please only choose one option')
if ops.__dict__['solver'] is not None and (ops.__dict__['compete'] is not None or ops.__dict__['player'] is not None):
    parser.error('Please only choose one option')
if ops.__dict__['compete'] is not None and (ops.__dict__['player'] is not None or ops.__dict__['solver'] is not None):
    parser.error('Please only choose one option')

def main():
    # put Game object in Player() ?
    # driver = Game()
    passenger = Player()

    # print( colored(' W ', 'white', 'on_grey') + colored(' O ', 'white', 'on_yellow') + colored(' R ', 'white', 'on_green') +
    # colored(' D ', 'white', 'on_grey') + colored(' L ', 'white', 'on_yellow') + colored(' E ', 'white', 'on_green'))

    guess = []
    print('Welcome to ' + colored(' W ', 'white', 'on_grey') + colored(' O ', 'white', 'on_yellow') + colored(' R ', 'white', 'on_green') +
           colored(' D ', 'white', 'on_grey') + colored(' L ', 'white', 'on_yellow') + colored(' E ', 'white', 'on_green'))

    # guess will be sent to our Player object
    # Player will store the array of Letters as a member
    # do the work inside of Player...
    passenger.runGame()


    exit(0)
    # create an array of Letter objects, which contain color info
    for i in range( 0, len(inguess)):
        guess.append( Letter( inguess[i], i))
    
    # Main Loop...
    # feedback = driver.nextGuess( guess)
    for i in feedback:
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

if __name__ == "__main__":
    main()
