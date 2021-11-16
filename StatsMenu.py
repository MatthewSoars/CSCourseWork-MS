import pygame
from ButtonClass import Button


class LogicStatsMenu:
    def __init__(self, screen):
        self.Screen = screen

        titleFont = pygame.font.SysFont('Comic Sans MS', 200)  # Sets the font and the size of font
        buttonFont = pygame.font.SysFont('Comic Sans MS', 35)  # Sets the font and the size of font
        statsFont = pygame.font.SysFont('Comic Sans MS', 90)  # Sets the font and the size of font
        self.textsurface = titleFont.render('Stats Menu', False, (0, 0, 0))  # Sets the parameters for the title
        self.DistanceText = statsFont.render('Distance Ran = Xm', True, (0, 0, 0))  # Sets parameters for the text
        self.coinsText = statsFont.render('Coins Collected = X', True, (0, 0, 0))  # Sets parameters for the text
        self.exitGameButton = buttonFont.render('Exit', True, (0, 0, 0))  # Sets parameters for the exit text

        self.exit_button = Button(550, 570, 280, 80, "Exit", self.Screen)

    def refresh(self, mouse_position):
        self.Screen.blit(self.textsurface, (150, 20))  # Displays stats screen title

        self.exit_button.refresh(mouse_position)

        # This next section relates to the super imposing of text onto the screen
        self.Screen.blit(self.DistanceText, (350, 240))  # Adds the distance text to the screen
        self.Screen.blit(self.coinsText, (350, 385))  # Adds the coins text to the screen

    def game_state_changer(self, mouse_position):
        if self.exit_button.button_press_checker(mouse_position):
            game_state = "MainMenu"
            return game_state

        else:
            game_state = "StatsMenu"
            return game_state
