# Imports the libraries needed for the screen to work
import pygame
from ButtonClass import Button

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

# Setting up the pygame window
pygame.init()  # initializing the imported module
MM = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters

# This section of the code creates fonts that can be used later
titleFont = pygame.font.SysFont('Comic Sans MS', 200)  # Sets the font and the size of font to be used for the title
buttonFont = pygame.font.SysFont('Comic Sans MS', 35)  # Sets the font and the size of font to be used for the buttons
statsFont = pygame.font.SysFont('Comic Sans MS', 90)  # Sets the font and the size of font to be used for the stats text
textsurface = titleFont.render('Stats Menu', False, (0, 0, 0))  # Sets the parameters for the title to be called later
DistanceText = statsFont.render('Distance Ran = Xm', True, (0, 0, 0))  # Sets parameters for the distance ran text
coinsText = statsFont.render('Coins Collected = X', True, (0, 0, 0))  # Parameters for the coins collected text
exitGameButton = buttonFont.render('Exit', True, (0, 0, 0))  # Sets parameters for the exit text

backGroundImage = pygame.image.load("Sprites/Background5.jpg").convert()  # Loading the background game sprite
backGroundPosition = 0  # Setting the backgrounds original position

exit_button = Button(550, 570, 280, 80, "Exit", MM)

running = True  # Sets the running boolean to true
# Game loop while the program is running
while running:

    mouse_position = pygame.mouse.get_pos()  # Gets the current position of the mouse and stores it

    # This section of code uses two backgrounds to create an infinite effect
    relativeBackGroundPosition = backGroundPosition % backGroundImage.get_rect().width  # Uses mod to move background
    MM.blit(backGroundImage, (relativeBackGroundPosition - backGroundImage.get_rect().width, 0))  # Blits the background
    if relativeBackGroundPosition < ScreenHeight:  # When relativeBackGroundPosition is more then ScreenHeight
        MM.blit(backGroundImage, (relativeBackGroundPosition, 0))  # Blits the second background image to the screen
    backGroundPosition -= 2  # Makes the background shift to the left

    MM.blit(textsurface, (150, 20))  # Displays stats screen title

    for event in pygame.event.get():  # Checks to see if any event in queue

        if event.type == pygame.QUIT:  # If event is quit
            running = False  # Set running bool to false

            # Next section of event recognition refers to the detection of button presses
            # This is for the game button calling the settings menu
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detects if the mouse button has been pressed
            exit_button.button_press_checker(mouse_position)

    exit_button.refresh(mouse_position)

    # This next section relates to the super imposing of text onto the screen
    MM.blit(DistanceText, (350, 240))  # Adds the distance text to the screen
    MM.blit(coinsText, (350, 385))  # Adds the coins text to the screen

    pygame.display.update()  # Updates the screen
