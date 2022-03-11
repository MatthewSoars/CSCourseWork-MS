# Importing the libraries/ Classes
import pygame  # Imports pygame
import time  # Imports the time library
from Logic import LogicBackground  # Imports the class needed for the background
from MainMenu import LogicMainMenu  # Imports the class needed for the MainMenu
from StatsMenu import LogicStatsMenu  # Imports the class needed for the StatsMenu
from SettingsMenu import LogicSettingsMenu  # Imports the class needed for the SettingsMenu
from ShopMenu import LogicShopMenu  # Imports the class needed for ShopMenu
from GameMenu import LogicGameMenu  # Imports the class needed for GameMenu
from bird import BirdClass  # Imports the bird character class
from boss import BossClass

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

game_state = "MainMenu"  # This allows me within the debugging stage of the development to boot the needed state

# Setting up the pygame window
pygame.init()  # initializing the imported module
screen = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters
Clock = pygame.time.Clock()  # Setups the pygame module for monitoring time

restart = False  # Sets restart to false

# Creates a sprite group
all_sprites = pygame.sprite.Group()  # Creates an all sprites group
mob_sprites = pygame.sprite.Group()  # Creates a mob sprite group
tube_hit_boxes = pygame.sprite.Group()  # Creates a tub_hit_box group
bullets_group = pygame.sprite.Group()  # Creates a tub_hit_box group
dragon_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

# Instantiates the screens for different states of the game
BackgroundLogic = LogicBackground()  # Instantiates the background class
MainMenuLogic = LogicMainMenu(screen)  # Instantiates the Main menu class
StatsMenuLogic = LogicStatsMenu(screen)  # Instantiates the Stats' menu class
SettingsMenuLogic = LogicSettingsMenu(screen)  # Instantiates the Settings menu class
ShopMenuLogic = LogicShopMenu(screen)  # Instantiates the Shop menu class
GameMenuLogic = LogicGameMenu(screen, all_sprites, mob_sprites, tube_hit_boxes, bullets_group, wall_group)  # Instantiates the Game menu class

# This section of the code instantiates the bird
PlayerSprite = BirdClass(screen, all_sprites, bullets_group)  # instantiates the bird class
player_group.add(PlayerSprite)

# This section of the code instantiates the boss
BossSprite = BossClass(screen, all_sprites, wall_group)
dragon_group.add(BossSprite)

# This section of the code creates fonts that can be used later
title_font = pygame.font.SysFont('Comic Sans MS', 110)  # Sets the font and the size of font
text_surface = title_font.render('Flighty Studios Presents', False, (255, 255, 255))  # Sets the parameters for the splash font
screen.blit(text_surface, (60, 250))  # Displays the splash text to the screen
pygame.display.update()  # Updates the screen
time.sleep(3)  # stops the program for three seconds

running = True  # Sets the running to true
while running:
    key_state = pygame.key.get_pressed()  # Gets the key which is pressed

    mouse_position = pygame.mouse.get_pos()  # Gets the current position of the mouse and stores it

    BackgroundLogic.refresh(screen, ScreenHeight)  # Refreshes the background logic object

    # The next section of code detects the current game state running/ changes game state
    if game_state == "MainMenu":  # If game state is MainMenu
        var = running == MainMenuLogic.refresh(mouse_position)  # Refreshes the Main menu class
        PlayerSprite.AutoFly()  # Calls the auto fly method to check if the method needs to take action

    elif game_state == "StatsMenu":  # If game state is StatsMenu
        var = running == StatsMenuLogic.refresh(mouse_position)  # Refreshes the Stats' menu class
        PlayerSprite.KillSprite()  # Kills the player sprite

    elif game_state == "SettingsMenu":  # If game state is SettingsMenu
        var = running == SettingsMenuLogic.refresh(mouse_position)  # Refreshes the Settings menu class
        PlayerSprite.KillSprite()  # Kills the player sprite

    elif game_state == "ShopMenu":  # If game state is SettingsMenu
        var = running == ShopMenuLogic.refresh(mouse_position)  # Refreshes the Settings menu class
        PlayerSprite.KillSprite()  # Kills the player sprite

    elif game_state == "GameMenu":  # If game state is GameMenu
        var = running == GameMenuLogic.refresh(game_state, PlayerSprite, mob_sprites)  # Refreshes the Game Menu class

    for event in pygame.event.get():  # Detects if a pygame event has been triggered
        if event.type == pygame.QUIT:  # If event is quit
            running = False  # Set running bool to false

        if event.type == pygame.KEYDOWN:  # Detects if a pygame key down event has been triggered
            if event.key == pygame.K_SPACE and game_state == "GameMenu":  # If space button has been pressed and in game
                PlayerSprite.Fly()  # Call a variation of the sprite refresh for the shop screen
            elif event.key == pygame.K_m and game_state == "GameMenu":  # If space button has been pressed and in game
                PlayerSprite.Shoot()  # Call a variation of the sprite refresh for the shop screen

        # Next section is used to check if the game state is needed to be changed
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detects if the mouse button has been pressed
            if game_state == "MainMenu":  # If the game state is MainMenu
                game_state = MainMenuLogic.game_state_change(mouse_position)  # Checks if the game state needs changing
            elif game_state == "StatsMenu":  # If the game state is StatsMenu
                game_state = StatsMenuLogic.game_state_changer(
                    mouse_position)  # Checks if the game state needs changing
                if game_state != "StatsMenu":  # If game state is Stats Menu
                    restart = True  # Sets restart to true to restart all the sprites
            elif game_state == "SettingsMenu":  # If the game state is Settings Menu
                game_state = SettingsMenuLogic.game_state_changer(mouse_position)  # Checks if game state needs changing
                if game_state != "SettingsMenu":  # If game state is Settings Menu
                    restart = True  # Sets restart to true to restart all the sprites
            elif game_state == "ShopMenu":  # If the game state is Shop Menu
                game_state = ShopMenuLogic.game_state_changer(mouse_position)  # Checks if game state needs changing
                if game_state != "ShopMenu":  # If game state is Shop Menu
                    restart = True  # Sets restart to true to restart all the sprites
            elif game_state == "GameMenu":  # If the game state is game menu
                game_state, restart = GameMenuLogic.game_state_change(mouse_position)  # Checks if game state needs changing

    # If restart is true
    if restart:
        PlayerSprite = BirdClass(screen, all_sprites, bullets_group)  # Instantiate a new Player sprite
        all_sprites.add(PlayerSprite)  # Adds the new player sprite to the screen
        restart = False  # Sets restart to false

    if game_state == "ShopMenu":  # If the game state is "Shop Menu"
        PlayerSprite.ShopScreen()  # Call a variation of the sprite refresh for the shop screen

    game_live = GameMenuLogic.GameLiveChecker()  # Checks to see if the game is live
    all_sprites.update(game_live)  # Updates all the sprites

    if game_state == "GameMenu":  # If the game state is game menu
        GameMenuLogic.TextUpdate()  # Method to superimpose text over game
        bullets_group.update(game_state)
        dragon_group.update(game_live)

    player_group.update(game_live)

    Clock.tick(60)  # Sets the FPS/ Clock tick
    pygame.display.update()  # Updates the screen
