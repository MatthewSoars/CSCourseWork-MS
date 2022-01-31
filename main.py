# Importing the libraries/ Classes
import pygame  # Imports pygame
from Logic import LogicBackground  # Imports the class needed for the background
from MainMenu import LogicMainMenu  # Imports the class needed for the MainMenu
from StatsMenu import LogicStatsMenu  # Imports the class needed for the StatsMenu
from SettingsMenu import LogicSettingsMenu  # Imports the class needed for the SettingsMenu
from ShopMenu import LogicShopMenu  # Imports the class needed for ShopMenu
from bird import BirdClass  # Imports the bird character class

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

game_state = "ShopMenu"  # This allows me within the debugging stage of the development to boot the needed state

# Setting up the pygame window
pygame.init()  # initializing the imported module
screen = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters
Clock = pygame.time.Clock()  # Setups the pygame module for monitoring time

# Instantiates the screens for different states of the game
BackgroundLogic = LogicBackground()  # Instantiates the background class
MainMenuLogic = LogicMainMenu(screen)  # Instantiates the Main menu class
StatsMenuLogic = LogicStatsMenu(screen)  # Instantiates the Stats' menu class
SettingsMenuLogic = LogicSettingsMenu(screen)  # Instantiates the Settings menu class
ShopMenuLogic = LogicShopMenu(screen)  # Instantiates the Shop menu class


# This section of the code instantiates the bird
PlayerSprite = BirdClass(screen)

running = True  # Sets the running to true
while running:
    key_state = pygame.key.get_pressed()  # Gets the key which is pressed

    mouse_position = pygame.mouse.get_pos()  # Gets the current position of the mouse and stores it

    BackgroundLogic.refresh(screen, ScreenHeight)  # Refreshes the background logic object

    # The next section of code detects the current game state running/ changes game state
    if game_state == "MainMenu":  # If game state is MainMenu
        var = running == MainMenuLogic.refresh(mouse_position)  # Refreshes the Main menu class
        PlayerSprite.AutoFly()

    elif game_state == "StatsMenu":  # If game state is StatsMenu
        var = running == StatsMenuLogic.refresh(mouse_position)  # Refreshes the Stats menu class

    elif game_state == "SettingsMenu":  # If game state is SettingsMenu
        var = running == SettingsMenuLogic.refresh(mouse_position)  # Refreshes the Settings menu class

    elif game_state == "ShopMenu":  # If game state is SettingsMenu
        var = running == ShopMenuLogic.refresh(mouse_position)  # Refreshes the Settings menu class

    for event in pygame.event.get():  # Detects if a pygame event has been triggered
        if event.type == pygame.QUIT:  # If event is quit
            running = False  # Set running bool to false

        # Next section is used to check if the game state is needed to be changed
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detects if the mouse button has been pressed
            if game_state == "MainMenu":  # If the game state is MainMenu
                game_state = MainMenuLogic.game_state_change(mouse_position)  # Checks if the game state needs changed
            elif game_state == "StatsMenu":  # If the game state is StatsMenu
                game_state = StatsMenuLogic.game_state_changer(mouse_position)  # Checks if the game state needs changed
            elif game_state == "SettingsMenu":  # If the game state is SettingsMenu
                game_state = SettingsMenuLogic.game_state_changer(mouse_position)  # Checks if game state needs changed
            elif game_state == "ShopMenu":  # If the game state is SettingsMenu
                game_state = ShopMenuLogic.game_state_changer(mouse_position)  # Checks if game state needs changed

    # Next section handles the sprite states
    if game_state != "ShopMenu":  # If the game state is anything but the Shop Menu
        PlayerSprite.Update()  # Call the standard sprite refresh method

    elif game_state == "ShopMenu":  # If the game state is "Shop Menu"
        PlayerSprite.ShopScreen()  # Call a variation of the sprite refresh for the shop screen

    Clock.tick(60)  # Sets the FPS/ Clock tick
    pygame.display.update()  # Updates the screen
