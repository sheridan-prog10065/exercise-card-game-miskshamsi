"""Defines the CardGameApp class"""

from game import CardGame

class CardGameApp:
    """Represents the card game application, responsible for starting and running the game
    
    Attributes (data/information):
        None
    Methods (functionality):
        running the game
        checking if the user wants to play again
    
    """

    def run(self):
        """Runs the application"""

        print('Welcome to the Python card game')

        #repeat playing game for as long as the user wants to keep playing
        playGame = True
        while playGame:
            #create the game object
            game = CardGame()

            #play the game
            game.play()

            #ask the user if they want to play again
            playGame = self.checkPlayAgain()

    
    def checkPlayAgain(self):
        """Asks the user if they want to play again and returns the answer to the caller"""

        #prompt the user if they want to play again
        playAgain = input('Do you want to play again? [y/n]')

        #return True/False depending on the user's answer
        if len(playAgain) > 0 and playAgain.lower()[0] == 'y':
            return True
        else: 
            return False
