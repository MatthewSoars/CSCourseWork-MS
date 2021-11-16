# Imports the libraries needed for the screen to work
import pygame
from ButtonClass import Button


class LogicMainMenu:
    def __init__(self, screen):
        self.Screen = screen

        # This section of the code creates fonts that can be used later
        titleFont = pygame.font.SysFont('Comic Sans MS', 200)  # Sets the font and the size of font
        buttonFont = pygame.font.SysFont('Comic Sans MS', 35)  # Sets the font and the size of font
        self.textsurface = titleFont.render('Birdy', False, (0, 0, 0))  # Sets the parameters for the title
        self.startGameButton = buttonFont.render('Start', True, (0, 0, 0))  # Sets parameters for the start button
        self.statsGameButton = buttonFont.render('Stats', True, (0, 0, 0))  # Sets parameters for the stats button
        self.shopGameButton = buttonFont.render('Shop', True, (0, 0, 0))  # Sets parameters for the shop button
        self.settingsGameButton = buttonFont.render('Settings', True, (0, 0, 0))  # Sets parameters for setting

        self.start_button = Button(550, 270, 280, 80, "Start", self.Screen)
        self.shop_button = Button(550, 370, 280, 80, "Shop", self.Screen)
        self.stats_button = Button(550, 470, 280, 80, "Stats", self.Screen)
        self.settings_button = Button(550, 570, 280, 80, "Settings", self.Screen)

    def refresh(self, mouse_position):
        self.Screen.blit(self.textsurface, (450, 20))  # Displays the title of the game to the screen
        self.start_button.refresh(mouse_position)
        self.shop_button.refresh(mouse_position)
        self.stats_button.refresh(mouse_position)
        self.settings_button.refresh(mouse_position)

    def game_state_change(self, mouse_position):
        if self.start_button.button_press_checker(mouse_position):
            game_state = "GameMenu"
            return game_state

        elif self.shop_button.button_press_checker(mouse_position):
            game_state = "ShopMenu"
            return game_state

        elif self.stats_button.button_press_checker(mouse_position):
            game_state = "StatsMenu"
            print(game_state)
            return game_state

        elif self.settings_button.button_press_checker(mouse_position):
            game_state = "SettingsMenu"
            return game_state

        else:
            game_state = "MainMenu"
            return game_state
