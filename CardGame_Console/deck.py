"""Defines the CardDeck class"""

from card import Card
import random

class CardDeck:
    """Represents a deck of cards

    Attributes (data/information):
        MAX_CARD_VALUE: class variable representing the maximum possible card value
        MAX_SUIT_COUNT: class variable representing the maximum suit in the deck
        _cardList: the list of cards in the deck

    Methods (functionality):
        creating a full card deck
        shuffling cards
        extracting cards
        exchanging cards
        printing the cards in the deck
    """

    #define the maximum possible card value
    MAX_CARD_VALUE = 13

    #define the maximum suit in the deck
    MAX_SUIT_COUNT = 4
        
    def __init__(self):
        """Constructor of the CardDeck reponsible for defining and initializing all its field variables"""

        self._cardList = []

        #create a full deck of cards
        self.createCards()

    def getCardCount(self):
        """Access the number of cards in the deck"""
        
        return len(self._cardList)
    
    def createCards(self):
        """Creates a complete deck with all the cards of every suit"""

        #repeat creating all cards for each suit (4 suits)
        for suit in range(1, CardDeck.MAX_SUIT_COUNT + 1):
            #repeat creating cards for each card values (13 values)
            for value in range(1, CardDeck.MAX_CARD_VALUE + 1):
                #create the card object
                card = Card(value, suit)

                #add the card to the deck
                self._cardList.append(card)
        
    
    def shuffleCards(self):
        """Shuffles the card deck using a Fisher-Yates shuffle algorithm
        https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
        """

        for iDeckPos in range(self.getCardCount()):
            #pick a random position in the deck higher than current position
            randIndex = random.randint(iDeckPos, len(self._cardList)-1)

            #swap the randomly chosen card (the card at the random index) with
            #the card in the current position
            crtCard = self._cardList[iDeckPos]
            self._cardList[iDeckPos] = self._cardList[randIndex]
            self._cardList[randIndex] = crtCard

    def getPairOfCards(self):
        """Extracts two random cards out of the deck. The cards are removed from the deck. 
        
        Returns a tuple of information (t1, t2, t3) where:
            t1: the first card extracted
            t2: the second card extracted
            t3: true/false, true if the cards were extracted and false otherwise
        
        """
        if (len(self._cardList) >= 2):
            #extract the first card
            cardOne = self._cardList.pop(random.randint(0, self.getCardCount() - 1))

            #extract the second card
            cardTwo = self._cardList.pop(random.randint(0, self.getCardCount() - 1))

            #return the cards as well as information whether the extraction worked
            return (cardOne, cardTwo, True)
        else:
            #extraction was not successful, no cards to return, let the client know
            return (None, None, False)        

    def exchangeCards(self, cardOne, cardTwo):
        """Exchange the given cards with each other"""
        return (cardTwo, cardOne)

    def printCards(self):
        """Print the deck of cards"""
        for card in self._cardList:
            #Good example of string formatting with the new formatted string literals.
            #See https://docs.python.org/3.6/whatsnew/3.6.html#whatsnew36-pep498       
            print(card)  

                

