# Imports the libraries needed for the screen to work
import pygame
from pygame.locals import *

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

# Setting up the pygame window
pygame.init()  # initializing the imported module
MM = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters

titleFont = pygame.font.SysFont('Comic Sans MS', 200)
buttonFont = pygame.font.SysFont('Comic Sans MS', 35)
textsurface = titleFont.render('Birdy', False, (0, 0, 0))
startGameButton = buttonFont.render('Start', True, (0, 0, 0))

backGroundImage = pygame.image.load("Sprites/Background5.jpg").convert()  # Loading the background game sprite
backGroundPosition = 0  # Setting the backgrounds original position

running = True  # Sets the running boolean to true
# Game loop while the program is running
while running:

    mousePosition = pygame.mouse.get_pos()

    # This section of code uses two backgrounds in order to create an infinite effect
    relativeBackGroundPosition = backGroundPosition % backGroundImage.get_rect().width  # Uses mod to move background
    MM.blit(backGroundImage, (relativeBackGroundPosition - backGroundImage.get_rect().width, 0))  # Blits the background
    if relativeBackGroundPosition < ScreenHeight:  # When relativeBackGroundPosition is more then ScreenHeight
        MM.blit(backGroundImage, (relativeBackGroundPosition, 0))  # Blits the second background image to the screen
    backGroundPosition -= 1  # Makes the background shift to the left

    MM.blit(textsurface, (450, 20))

    for event in pygame.event.get():  # Checks to see if any event in queue

        if event.type == pygame.QUIT:  # If event is quit
            running = False  # Set running bool to false

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ScreenWidth/2 <= mousePosition[0] <= ScreenWidth and ScreenHeight/2 <= mousePosition[1]:
                pygame.quit()

    # This next section of code relates to the start buttons detection of the mouse when hovered over
    if 550 <= mousePosition[0] <= 550 + 280:
        if 350 <= mousePosition[1] <= 350 + 80:
            pygame.draw.rect(MM, (170, 170, 170), [550, 350, 280, 80])

        else:
            pygame.draw.rect(MM, (100, 100, 100), [550, 350, 280, 80])
    else:
        pygame.draw.rect(MM, (100, 100, 100), [550, 350, 280, 80])

    MM.blit(startGameButton, (650, 360))  # Super imposes the Start text on the start game button

    pygame.display.update()  # Updates the screen
