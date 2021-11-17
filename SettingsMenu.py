# Imports the libraries needed for the screen to work
import pygame
from VolumeSliderClass import VolumeSlider
from ButtonClass import Button


class LogicSettingsMenu:
    def __init__(self, screen):
        self.music_volume = 0
        self.master_volume = 0

        self.screen = screen

        # This section of the code creates fonts that can be used later
        titleFont = pygame.font.SysFont('Comic Sans MS', 150)  # Sets the font and the size of font for the title
        self.textsurface = titleFont.render('Settings', False, (0, 0, 0))  # Sets the parameters for the title text

        self.MusicSlider = VolumeSlider(200, "Music", screen)
        self.MasterSlider = VolumeSlider(400, "Master", screen)
        self.exit_button = Button(550, 590, 280, 80, "Exit", screen)

    def refresh(self, mouse_position):
        self.screen.blit(self.textsurface, (375, -10))  # Displays stats screen title

        self.MusicSlider.hover(mouse_position)
        self.MusicSlider.refresh(self.music_volume, self.master_volume)
        self.MasterSlider.hover(mouse_position)
        self.MasterSlider.refresh(self.music_volume, self.master_volume)
        self.exit_button.refresh(mouse_position)

    def game_state_changer(self, mouse_position):
        self.music_volume = self.MusicSlider.button_press_checker(self.music_volume, mouse_position)
        self.master_volume = self.MasterSlider.button_press_checker(self.master_volume, mouse_position)
        if self.exit_button.button_press_checker(mouse_position):
            game_state = "MainMenu"
            return game_state

        else:
            game_state = "SettingsMenu"
            return game_state
