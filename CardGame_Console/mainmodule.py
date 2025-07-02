"""Represents the entry point in the application. The module is responsible for creating and running the app"""

from application import CardGameApp

#create the card game app
app = CardGameApp()

#ask the card game app to run. This allows the app to be a purely object-oriented program
#as the first actual statement that is executed is part of method 
app.run()