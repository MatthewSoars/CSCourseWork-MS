# Imports the libraries needed for the screen to work
import pygame
from ButtonClass import Button
from Background import parallax_effect

screen_height = 1366  # Sets the screens height
screen_width = 768  # Sets the screens width

# Setting up the pygame window
pygame.init()  # initializing the imported module
MM = pygame.display.set_mode((screen_height, screen_width))  # Displaying a window of set parameters

# This section of the code creates fonts that can be used later
titleFont = pygame.font.SysFont('Comic Sans MS', 200)  # Sets the font and the size of font to be used for the title
buttonFont = pygame.font.SysFont('Comic Sans MS', 35)  # Sets the font and the size of font to be used for the buttons
textsurface = titleFont.render('Birdy', False, (0, 0, 0))  # Sets the parameters for the title to be called later
startGameButton = buttonFont.render('Start', True, (0, 0, 0))  # Sets parameters for the start button to be called later
statsGameButton = buttonFont.render('Stats', True, (0, 0, 0))  # Sets parameters for the stats button to be called later
shopGameButton = buttonFont.render('Shop', True, (0, 0, 0))  # Sets parameters for the shop button to be called later
settingsGameButton = buttonFont.render('Settings', True, (0, 0, 0))  # Sets parameters for setting button for later

back_ground_image = pygame.image.load("Sprites/Background5.jpg").convert()  # Loading the background game sprite
back_ground_position = 0  # Setting the backgrounds original position

start_button = Button(550, 270, 280, 80, "Start", MM)
shop_button = Button(550, 370, 280, 80, "Shop", MM)
stats_button = Button(550, 470, 280, 80, "Stats", MM)
settings_button = Button(550, 570, 280, 80, "Settings", MM)

running = True  # Sets the running boolean to true
# Game loop while the program is running
while running:

    mouse_position = pygame.mouse.get_pos()  # Gets the current position of the mouse and stores it

    parallax_effect(MM, back_ground_position, back_ground_image, screen_height)

    MM.blit(textsurface, (450, 20))  # Displays the title of the game to the screen

    for event in pygame.event.get():  # Checks to see if any event in queue

        if event.type == pygame.QUIT:  # If event is quit
            running = False  # Set running bool to false

        # Next section of event recognition refers to the detection of button presses
        # This is for the game button calling the game to play
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detects if the mouse button has been pressed
            start_button.button_press_checker(mouse_position)
            shop_button.button_press_checker(mouse_position)
            stats_button.button_press_checker(mouse_position)
            settings_button.button_press_checker(mouse_position)

    start_button.refresh(mouse_position)
    shop_button.refresh(mouse_position)
    stats_button.refresh(mouse_position)
    settings_button.refresh(mouse_position)

    pygame.display.update()  # Updates the screen
