# Class to hold information about individual letters
# James Natoli, 2022

class letter:
    def __init__(self):
        """Initialize to nothing"""
        text = ''
        color = ''
        position = 0

    def __init__(self, t1, p1, c1='red'):
        """Alternate initialization"""
        self.text = t1
        self.position = p1
        self.color = c1
        
    def getPos( self):
        """Get the letters position"""
        return self.position

    def getText( self):
        """Get the text associated with the letter"""
        return self.text

    def getColor( self):
        """Get the letters color"""
        return self.color

    def setColor( self, newcol):
        """Set the letters color"""
        self.color = newcol
    
    def print( self):
        """Hmm..."""
        getText( self)
