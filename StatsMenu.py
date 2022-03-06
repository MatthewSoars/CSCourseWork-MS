# Imports the libraries needed for the screen to work
import pygame  # Imports the pygame library
from ButtonClass import Button  # Imports the button class


# Code for the class of the stats menu
class LogicStatsMenu:
    def __init__(self, screen):  # Function called when class is instantiated
        self.Screen = screen  # Gets the screen that is needed to be added to

        # This section of the code creates fonts that can be used later
        title_font = pygame.font.SysFont('Comic Sans MS', 200)  # Sets the font and the size of font
        stats_font = pygame.font.SysFont('Comic Sans MS', 90)  # Sets the font and the size of font
        self.text_surface = title_font.render('Stats Menu', False, (0, 0, 0))  # Sets the parameters for the title
        self.DistanceText = stats_font.render('Distance Flown = X', True, (0, 0, 0))  # Sets parameters for the text
        self.coinsText = stats_font.render('Coins Collected = X', True, (0, 0, 0))  # Sets parameters for the text

        # This section of the code instantiates the buttons
        self.exit_button = Button(550, 570, 280, 80, "Exit", self.Screen)  # Sets parameters for the exit button

    def refresh(self, mouse_position):    # Function to refresh the main menu
        self.Screen.blit(self.text_surface, (150, 20))  # Displays stats screen title

        self.exit_button.refresh(mouse_position)  # Updates the exit button

        # This next section relates to the superimposing of text onto the screen
        self.Screen.blit(self.DistanceText, (350, 240))  # Adds the distance text to the screen
        self.Screen.blit(self.coinsText, (350, 385))  # Adds the coins text to the screen

    def game_state_changer(self, mouse_position):  # Function to change the game state
        if self.exit_button.button_press_checker(mouse_position):  # If exit button is pressed
            game_state = "MainMenu"  # Sets the game state to 'MainMenu'
            return game_state  # Returns the game_state

        else:
            game_state = "StatsMenu"  # Sets the game state to 'StatsMenu'
            return game_state  # Returns the game_state
