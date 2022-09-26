# Class to hold information about individual letters
# James Natoli, 2022

from termcolor import colored
from colorMap import colorMap

class Letter:
    def __init__(self):
        """Initialize to nothing"""
        text = ''
        color = 'on_grey'
        position = 0

    def __init__(self, txt, pos, col='on_red'):
        """Alternate initialization"""
        self.text = txt
        self.position = pos
        self.color = col
        
    def getPos( self):
        """Get the letters position"""
        return self.position

    def getText( self):
        """Get the text associated with the letter"""
        return self.text

    def getColor( self):
        """Get the letters color"""
        return self.color

    def setColor( self, newColID):
        """Set the letters color"""
        self.color = colorMap[newColID]

    
    def __str__( self):
        """Return the 'colored' object for this letter"""
        return colored(' %s ', 'white', '%s'%( self.text, self.color))
