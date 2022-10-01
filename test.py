# Driver for Wordle Game
# James Natoli, 2022

from optparse  import OptionParser
from termcolor import colored, cprint

# Local Classes
# from Game import Game
from Player import Player
from Letter import Letter

parser = OptionParser()
parser.add_option('--player', '-p', action='store_true', 
                  help='Choose this option if you want to play as a Player')
parser.add_option('--solver', '-s', action='store_true', 
                  help='Choose this option if you want to watch the Solver')
parser.add_option('--compete', '-c', action='store_true',
                  help='Choose this option if you want to compete with the Solver')
parser.add_option('--wordlength', '-l', action='store', default=5, type=int,
                  help='Provide a number here to use different lengths of words')
(ops, args) = parser.parse_args()

if ops.__dict__['player'] is not None and (ops.__dict__['solver'] is not None or ops.__dict__['compete'] is not None):
    parser.error('Please only choose one option')
if ops.__dict__['solver'] is not None and (ops.__dict__['compete'] is not None or ops.__dict__['player'] is not None):
    parser.error('Please only choose one option')
if ops.__dict__['compete'] is not None and (ops.__dict__['player'] is not None or ops.__dict__['solver'] is not None):
    parser.error('Please only choose one option')

def main():
    passenger = Player( int(ops.__dict__['wordlength']))
    passenger.runGame()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as kExcept:
        print( kExcept)
        print("\n Thanks for playing!")
    except Exception as e:
        print( e)
        print("\n\nBye Bye!")
        exit(0)
