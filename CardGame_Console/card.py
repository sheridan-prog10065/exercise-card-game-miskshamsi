"""Defines the Card class"""

class Card:
    """Represents a card in a card game

    Attributes (data/information):
        DIAMOND, CLUB, HEART, SPADE: class variables representing the card suits
        _value: the value of the card, from 1 to 14
        _suit: the suit of the card, from 1 to 4

    Methods (functionality):
        accessing the value and suit of the card
        getting the name of the card (e.g. Queen for 12)
        getting the name of the suit (e.g. Spades for 4)
        string representation of the card (e.g. Ace of Spades, 3 of Diamonds)        
    """

    #define the suite values as class variables which are constant
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4

    def __init__(self, value, suit):
        """Creates and initializes the attributes of the card object"""

        self._value = value
        self._suit = suit 
    
    def getValue(self):
        """Access the value of the card"""

        return self._value

    def setValue(self, newValue):
        """Change the value of the card"""

        self._value = newValue

    def getSuit(self):
        """Access the suit of the card"""

        return self._suit

    def setSuit(self, newSuit):
        """Change the suit of the card"""

        self._suit = newSuit

    def getCardName(self):
        """Determines the card name based on the card value. 
        
        The name of the card is an example  of a calculated property that is 
        never stored as a separte field variable. Such property is also called 
        a derived attribute
        
        """

        if (self._value == 1):
            cardName = 'Ace'
        elif (self._value == 13):
            cardName = 'King'
        elif (self._value == 12):
            cardName = 'Queen'
        elif (self._value == 11):
            cardName = 'Jack'
        else:
            cardName = str(self._value)
        
        #return the calculated card name to the caller
        return cardName

    def getSuitName(self):
        """Determine the name of the suit of the card based on the suit value"""

        if self._suit == Card.DIAMONDS:
            return 'Diamonds'
        elif self._suit == Card.CLUBS:
            return 'Clubs'
        elif self._suit == Card.HEARTS:
            return 'Hearts'
        elif self._suit == Card.SPADES:
            return 'Spades'
        else:
            assert False, 'Unknown suit value. Cannot return the suit name'

    def __str__(self):
        """Default built-in method that is called automatically when a card object is printed"""
        return f'{self.getCardName()} of {self.getSuitName()}'

