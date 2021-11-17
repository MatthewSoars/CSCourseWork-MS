import pygame
from Logic import LogicBackground
from MainMenu import LogicMainMenu
from StatsMenu import LogicStatsMenu
from SettingsMenu import LogicSettingsMenu

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

game_state = "MainMenu"

# Setting up the pygame window
pygame.init()  # initializing the imported module
screen = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters
Clock = pygame.time.Clock()

BackgroundLogic = LogicBackground()
MainMenuLogic = LogicMainMenu(screen)
StatsMenuLogic = LogicStatsMenu(screen)
SettingsMenuLogic = LogicSettingsMenu(screen)

running = True
while running:
    mouse_position = pygame.mouse.get_pos()  # Gets the current position of the mouse and stores it

    BackgroundLogic.refresh(screen, ScreenHeight)

    if game_state == "MainMenu":
        var = running == MainMenuLogic.refresh(mouse_position)

    elif game_state == "StatsMenu":
        var = running == StatsMenuLogic.refresh(mouse_position)

    elif game_state == "SettingsMenu":
        var = running == SettingsMenuLogic.refresh(mouse_position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If event is quit
            running = False  # Set running bool to false

        if event.type == pygame.MOUSEBUTTONDOWN:  # Detects if the mouse button has been pressed
            if game_state == "MainMenu":
                game_state = MainMenuLogic.game_state_change(mouse_position)
            elif game_state == "StatsMenu":
                game_state = StatsMenuLogic.game_state_changer(mouse_position)
            elif game_state == "SettingsMenu":
                game_state = SettingsMenuLogic.game_state_changer(mouse_position)

    Clock.tick(60)
    pygame.display.update()  # Updates the screen
