# Imports the libraries needed for the screen to work
import pygame

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

# Setting up the pygame window
pygame.init()  # initializing the imported module
MM = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters

# Section creates fonts and texts that can be used later to create a game loop
titleFont = pygame.font.SysFont('Comic Sans MS', 200)  # Sets the font and the size of font to be used for the title
buttonFont = pygame.font.SysFont('Comic Sans MS', 35)  # Sets the font and the size of font to be used for the buttons
textsurface = titleFont.render('Birdy', False, (0, 0, 0))  # Sets the parameters for the title to be called later
startGameButton = buttonFont.render('Start', True, (0, 0, 0))  # Sets parameters for the start button to be called later
statsGameButton = buttonFont.render('Stats', True, (0, 0, 0))  # Sets parameters for the stats button to be called later
shopGameButton = buttonFont.render('Shop', True, (0, 0, 0))  # Sets parameters for the shop button to be called later
settingsGameButton = buttonFont.render('Settings', True, (0, 0, 0))  # Sets parameters for setting button for later

backGroundImage = pygame.image.load("Sprites/Background5.jpg").convert()  # Loading the background game sprite
backGroundPosition = 0  # Setting the backgrounds original position

running = True  # Sets the running boolean to true
# Game loop while the program is running
while running:

    mousePosition = pygame.mouse.get_pos()  # Gets the current position of the mouse and stores it

    # This section of code uses two backgrounds to create an infinite effect
    relativeBackGroundPosition = backGroundPosition % backGroundImage.get_rect().width  # Uses mod to move background
    MM.blit(backGroundImage, (relativeBackGroundPosition - backGroundImage.get_rect().width, 0))  # Blits the background
    if relativeBackGroundPosition < ScreenHeight:  # When relativeBackGroundPosition is more then ScreenHeight
        MM.blit(backGroundImage, (relativeBackGroundPosition, 0))  # Blits the second background image to the screen
    backGroundPosition -= 1  # Makes the background shift to the left

    pygame.display.update()  # Updates the screen
