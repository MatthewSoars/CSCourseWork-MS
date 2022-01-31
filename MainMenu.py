# Imports the libraries needed for the screen to work
import pygame  # Imports the pygame library
from ButtonClass import Button  # Imports the button class


# Code for the class of the main menu
class LogicMainMenu:
    def __init__(self, screen):  # Method called when class is instantiated
        self.Screen = screen  # Gets the screen that is needed to be added to

        # This section of the code creates fonts that can be used later
        title_font = pygame.font.SysFont('Comic Sans MS', 200)  # Sets the font and the size of font
        self.text_surface = title_font.render('Birdy', False, (0, 0, 0))  # Sets the parameters for the title

        # This section of the code instantiates the buttons
        self.start_button = Button(550, 270, 280, 80, "Start", self.Screen)  # Instantiates the start button
        self.shop_button = Button(550, 370, 280, 80, "Shop", self.Screen)   # Instantiates the shop button
        self.stats_button = Button(550, 470, 280, 80, "Stats", self.Screen)  # Instantiates the stats button
        self.settings_button = Button(550, 570, 280, 80, "Settings", self.Screen)  # Instantiates the settings button

    def refresh(self, mouse_position):  # Method to refresh the main menu
        self.Screen.blit(self.text_surface, (450, 20))  # Displays the title of the game to the screen
        self.start_button.refresh(mouse_position)  # Updates the start button
        self.shop_button.refresh(mouse_position)  # Updates the shop button
        self.stats_button.refresh(mouse_position)  # Updates the stats button
        self.settings_button.refresh(mouse_position)  # Updates the settings button

    def game_state_change(self, mouse_position):  # Method to change the game state
        if self.start_button.button_press_checker(mouse_position):  # If start button is pressed
            game_state = "GameMenu"  # Sets the game state to 'GameMenu'
            return game_state  # Returns the game_state

        elif self.shop_button.button_press_checker(mouse_position):  # If shop button is pressed
            game_state = "ShopMenu"  # Sets the game state to 'ShopMenu'
            return game_state  # Returns the game_state

        elif self.stats_button.button_press_checker(mouse_position):  # If stats button is pressed
            game_state = "StatsMenu"  # Sets the game state to 'StatsMenu'
            return game_state  # Returns the game_state

        elif self.settings_button.button_press_checker(mouse_position):  # If settings button is pressed
            game_state = "SettingsMenu"  # Sets the game state to 'StatsMenu'
            return game_state  # Returns the game_state

        else:
            game_state = "MainMenu"  # Sets the game state to 'MainMenu'
            return game_state  # Returns the game_state
