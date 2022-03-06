# Imports the libraries needed for the screen to work
import pygame  # Imports the pygame library
from ButtonClass import Button  # Imports the button class
import shelve  # Imports the shelve class


# Code for the class of the stats menu
class LogicStatsMenu:
    def __init__(self, screen):  # Function called when class is instantiated
        self.Screen = screen  # Gets the screen that is needed to be added to

        # This section of the code creates fonts that can be used later
        self.title_font = pygame.font.SysFont('Comic Sans MS', 200)  # Sets the font and the size of font
        self.stats_font = pygame.font.SysFont('Comic Sans MS', 90)  # Sets the font and the size of font
        self.text_surface = self.title_font.render('Stats Menu', False, (0, 0, 0))  # Sets the parameters for the title

        # This section of the code instantiates the buttons
        self.exit_button = Button(550, 570, 280, 80, "Exit", self.Screen)  # Sets parameters for the exit button
        self.high_score_reset_button = Button(950, 570, 280, 80, "Score Reset", self.Screen)  # Sets parameters for the high score button
        self.distance_reset_button = Button(150, 570, 280, 80, "Distance Reset", self.Screen)  # Sets parameters for the distance button

    def refresh(self, mouse_position):    # Function to refresh the main menu

        txt_doc = shelve.open('scores.txt')  # here you will save the score variable
        score = txt_doc['score']  # the score is read from disk
        distance = txt_doc['distance']  # the distance is read from the disk
        txt_doc.close()  # Closes the file
        high_score = str("High Score =" + str(score))  # Sets the high score variable
        distance = str("Distance =" + str(distance))  # Sets the distance variable
        distance_text = self.stats_font.render(distance, True, (0, 0, 0))  # Sets parameters for the text
        high_score_text = self.stats_font.render(high_score, True, (0, 0, 0))  # Sets parameters for the text

        self.Screen.blit(self.text_surface, (150, 20))  # Displays stats screen title

        self.exit_button.refresh(mouse_position)  # Updates the exit button
        self.high_score_reset_button.refresh(mouse_position)  # Updates the high score button
        self.distance_reset_button.refresh(mouse_position)  # Updates the distance button

        # This next section relates to the superimposing of text onto the screen
        self.Screen.blit(distance_text, (350, 240))  # Adds the distance text to the screen
        self.Screen.blit(high_score_text, (350, 385))  # Adds the coins text to the screen

    def game_state_changer(self, mouse_position):  # Function to change the game state
        if self.high_score_reset_button.button_press_checker(mouse_position):  # If high score reset is pressed
            txt_doc = shelve.open('scores.txt')  # Opens the score txt
            txt_doc['score'] = 0  # New high score is saved to disk
            txt_doc.close()  # Closes the txt file

        elif self.distance_reset_button.button_press_checker(mouse_position):  # If high score reset is pressed
            txt_doc = shelve.open('scores.txt')  # Opens the score txt
            txt_doc['distance'] = 0  # New high score is saved to disk
            txt_doc.close()  # Closes the txt file

        if self.exit_button.button_press_checker(mouse_position):  # If exit button is pressed
            game_state = "MainMenu"  # Sets the game state to 'MainMenu'
            return game_state  # Returns the game_state

        else:
            game_state = "StatsMenu"  # Sets the game state to 'StatsMenu'
            return game_state  # Returns the game_state
