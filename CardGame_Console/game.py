"""Defines the CardGame class which defines the logic of the card game"""

from deck import CardDeck

class CardGame:
    """Represents the game itself and implement the card game logic

    Attributes (data/information):
        _cardDeck: the list of cards in the deck
        _playerScore: the score of the player
        _houseScore: the score of the house
        _playerCard: the card being played by the player in the current round
        _houseCard: the card being played by the house in the current round
        
    Methods (functionality):
        - access methods for cards being played and scores
        - checking winner and whether the game is done
        - dealing cards
        - game play
    """

    def __init__(self):
        """Initialize the game objects and its attributes"""

        #define the deck used in the card game
        self._cardDeck = CardDeck()
        
        #keep track of the score of the player and the house
        self._playerScore = 0
        self._houseScore = 0

        #track the current hand, the cards currently in play in the current round
        self._playerCard = None
        self._houseCard = None   

    def getPlayerScore(self):
        """Access the score of the player"""

        return self._playerScore

    def getHouseScore(self):
        """Access the score of the house"""

        return self._houseScore

    def getPlayerCard(self):
        """Access the card being played by the player in the current round"""

        return self._playerCard

    def getHouseCard(self):
        """Access the card being played by the house in the current round"""

        return self._houseCard

    def playerWins(self):
        """Check whether the player won the game"""

        return self.isOver() and self._playerScore > self._houseScore

    def houseWins(self):
        """Check whether the house won the game"""

        return self.isOver() and self._houseScore > self._playerScore

    def isOver(self):
        """Check whether the game is over"""

        return self._cardDeck.getCardCount() < 2

    def dealCards(self):
        """Deals cards to the player and the house"""

        self._playerCard, self._houseCard, cardsDealt = self._cardDeck.getPairOfCards()
        if not cardsDealt:
            assert false, 'Unexpected call to playRound(). The cards cannot be dealt which may mean the game is over'
            return 0
        print(f'Cards for the round are dealt.')

    def switchCards(self):
        """Switches the card of the player with the card of the house"""

        self._playerCard, self._houseCard = self._cardDeck.exchangeCards(self._playerCard, self._houseCard)

    def play(self):
        """Plays the game rounds until no more cards are left keeping the score."""

        #shuffle the cards
        self._cardDeck.shuffleCards()

        while not self.isOver():
            #game still in progress, play another round
            roundResult = self.playRound()

            #show the result of the round
            self.showRoundResult(roundResult)           
        else:
            #game is over
            self.showGameOver()

    def playRound(self):
        """Plays a round in the game
        Returns:
            +1: the player won the round
            -1: the house won the round
             0: the round was a draw 
        """
        #show the beginning of the round
        print('\n', '-'*80, '\n', sep='')
        
        #deal the cards for the round
        self.dealCards()
 
        #give the user an opportunity to exchange the cardsDealt
        exchangeInput = input('Do you want to exchange the cards with the house [y/n]?')
        if len(exchangeInput) > 0 and exchangeInput.lower()[0] == 'y':
            self.switchCards()

        #determine the rank of the card which may be different than its value (e.g. Ace is 1)
        playerCardRank = self.determineCardRank(self._playerCard)
        houseCardRank = self.determineCardRank(self._houseCard)

        #compare the player card with the house card to see which one wins the round
        if playerCardRank > houseCardRank:
            #the player won the round, update the score
            self._playerScore += 1
            return 1
        elif houseCardRank > playerCardRank:
            #the house won the card, update the score
            self._houseScore += 1
            return -1
        else:
            #the player and house card values are the same. The round is a draw.
            return 0

    def determineCardRank(self, card):
        """Determines the ranks cards have in the game based on their value and suit"""

        #use the ternary operator to return the value of a conditional expression
        #that ensures the Ace is the highest card value in this game. 
        return 14 if card.getValue() == 1 else card.getValue()
     
    def showRoundResult(self, roundResult):
        """Displays the result of a game round"""
        
        #inform the user what is the result of the round
        if roundResult == 1:
            print(f'Player won the round with card "{self.getPlayerCard()}" against "{self.getHouseCard()}".')
        elif roundResult == -1:
            print(f'House won the round with the card "{self.getHouseCard()}" against "{self.getPlayerCard()}".')
        elif roundResult == 0:
            print(f'The round was a draw. The user had "{self.getPlayerCard()}" and the house had "{self.getHouseCard()}"')
        else:
            assert false, 'Unexpected game round play result.'
        
        #show the updated score
        print(f'The score is {self.getPlayerScore()} (user) to {self.getHouseScore()} (house)')


    def showGameOver(self):
        """Displays the winner information at the end of the game"""

        #defensive programming best practice: make sure the method is called in the correct state of the game
        assert self.isOver(), 'The game must be over in order to call this method'

        if self.playerWins():
            print('GameOver\nPlayer Wins!')
        elif self.houseWins():
            print('Game Over!\nHouse Wins!')
        else:
            print('Game Over!\nThe Game Is a Draw')
