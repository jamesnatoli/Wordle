# Class to hold information about individual letters
# James Natoli, 2022

from termcolor import colored
from colorMap import colorMap

class Letter:
    def __init__(self):
        """Initialize to nothing"""
        self.text = ''
        self.color = 'on_grey'
        self.position = 0

    def __init__(self, txt, pos, col='on_grey'):
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

    def setText( self, newText):
        """Set the letters text"""
        self.text = newText.capitalize()
    
    def setColor( self, newColID):
        """Set the letters color"""
        self.color = colorMap[newColID]
    
    def __str__( self):
        """Return the 'colored' object for this letter"""
        return colored(' %s '%( self.text), 'white', '%s'%(self.color))

    def __repr__(self):
        """Return string representation"""
        return self.__str__()
