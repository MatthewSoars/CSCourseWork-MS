# Imports the libraries needed for the screen to work
import pygame  # Imports the pygame library
from ButtonClass import Button  # Imports the button class


# Code for the class of the stats menu
class LogicShopMenu:
    def __init__(self, screen):  # Function called when class is instantiated
        self.Screen = screen  # Gets the screen that is needed to be added to

        # This section of the code creates fonts that can be used later
        title_font = pygame.font.SysFont('Comic Sans MS', 150)  # Sets the font and the size of font
        self.text_surface = title_font.render('Shop Menu', False, (0, 0, 0))  # Sets the parameters for the title
        self.left_button = Button(350, 325, 150, 80, "Left", self.Screen)  # Sets the parameters for the left button
        self.right_button = Button(850, 325, 150, 80, "Right", self.Screen)  # Sets the parameters for the right button

        # This section of the code instantiates the buttons
        self.exit_button = Button(550, 570, 280, 80, "Exit", self.Screen)  # Sets parameters for the exit button

    def refresh(self, mouse_position):  # Function to refresh the main menu
        self.Screen.blit(self.text_surface, (300, 20))  # Displays stats screen title
        self.exit_button.refresh(mouse_position)  # Updates the exit button
        self.left_button.refresh(mouse_position)  # Updates the left button
        self.right_button.refresh(mouse_position)  # Updates the right button

    def game_state_changer(self, mouse_position):  # Function to change the game state
        if self.exit_button.button_press_checker(mouse_position):  # If exit button is pressed
            game_state = "MainMenu"  # Sets the game state to 'MainMenu'
            return game_state  # Returns the game_state

        else:
            game_state = "ShopMenu"  # Sets the game state to 'StatsMenu'
            return game_state  # Returns the game_state
