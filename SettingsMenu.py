# Imports the libraries needed for the screen to work
import pygame  # Imports the pygame library
from VolumeSliderClass import VolumeSlider  # Imports the volume class
from ButtonClass import Button  # Imports the button class
from MusicLogic import LogicMusic  # Imports the class needed for music logic


# Code for the class of the logic menu
class LogicSettingsMenu:
    def __init__(self, screen):  # Function called when class is instantiated
        self.music_volume = 1  # Sets the initial music volume
        self.master_volume = 1  # Sets the initial master volume

        self.screen = screen  # Gets the screen that is needed to be added to

        # This section of the code creates fonts that can be used later
        title_font = pygame.font.SysFont('Comic Sans MS', 150)  # Sets the font and the size of font for the title
        self.text_surface = title_font.render('Settings', False, (0, 0, 0))  # Sets the parameters for the title text

        # This section of the code instantiates the buttons / Sliders
        self.MusicSlider = VolumeSlider(200, "Music", screen)  # Instantiates the Music Slider
        self.MasterSlider = VolumeSlider(400, "Master", screen)  # Instantiates the Master Slider
        self.exit_button = Button(550, 590, 280, 80, "Exit", screen)  # Instantiates the Exit Button

        # Deals with controlling the logic for the music
        self.music_controller = LogicMusic()  # Instantiates the class of the music controller starting music 

    def refresh(self, mouse_position):  # Function to refresh the Settings Menu
        self.screen.blit(self.text_surface, (375, -10))  # Displays stats screen title

        self.MusicSlider.hover(mouse_position)  # Detects the hovering of the mouse over the Master Slider
        self.MusicSlider.refresh(self.music_volume, self.master_volume)  # Updates the Music Slider
        self.MasterSlider.hover(mouse_position)  # Detects the hovering of the mouse over the Master Slider
        self.MasterSlider.refresh(self.music_volume, self.master_volume)  # Updates the Master Slider
        self.exit_button.refresh(mouse_position)  # Updates the exit button
        
        self.music_controller.volume_change(self.music_volume)

    def game_state_changer(self, mouse_position):  # Function to change the game state
        # Changes the music volume
        self.music_volume = self.MusicSlider.button_press_checker(self.music_volume, mouse_position)
        # Changes the master volume
        self.master_volume = self.MasterSlider.button_press_checker(self.master_volume, mouse_position)
        if self.exit_button.button_press_checker(mouse_position):  # If exit button is pressed
            game_state = "MainMenu"  # Sets the game state to 'MainMenu'
            return game_state  # Returns the game_state

        else:
            game_state = "SettingsMenu"  # Sets the game state to 'SettingsMenu'
            return game_state  # Returns the game_state
