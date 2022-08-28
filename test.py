# Driver for Wordle Game
# James Natoli, 2022

from optparse import OptionParser

# Local Classes
from Game import Game
from Player import Player

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
    driver = Game()
    passenger = Player()

if __name__ == "__main__":
    main()
