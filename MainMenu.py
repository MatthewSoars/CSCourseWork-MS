# Imports the libraries needed for the screen to work
import pygame

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

# Setting up the pygame window
pygame.init()  # initializing the imported module
MM = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters

# This section of the code creates fonts that can be used later
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

    MM.blit(textsurface, (450, 20))  # Displays the title of the game to the screen

    for event in pygame.event.get():  # Checks to see if any event in queue

        if event.type == pygame.QUIT:  # If event is quit
            running = False  # Set running bool to false

        # Next section of event recognition refers to the detection of button presses
        # This is for the game button calling the game to play
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detects if the mouse button has been pressed
            if 550 <= mousePosition[0] <= 550 + 280:  # Detects if mouse position x is within set bounds
                if 270 <= mousePosition[1] <= 270 + 80:  # Detects if mouse position y is within set bounds
                    print("Game")  # This is where the code calling the game to play goes

        # This is for the game button calling the shop menu
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detects if the mouse button has been pressed
            if 550 <= mousePosition[0] <= 550 + 280:  # Detects if mouse position x is within set bounds
                if 370 <= mousePosition[1] <= 370 + 80:  # Detects if mouse position y is within set bounds
                    print("Shop")  # This is where the code calling the shop menu

            # This is for the game button calling the stats menu
            if event.type == pygame.MOUSEBUTTONDOWN:  # Detects if the mouse button has been pressed
                if 550 <= mousePosition[0] <= 550 + 280:  # Detects if mouse position x is within set bounds
                    if 470 <= mousePosition[1] <= 470 + 80:  # Detects if mouse position y is within set bounds
                        print("Stats")  # This is where the code calling the stats menu

            # This is for the game button calling the settings menu
            if event.type == pygame.MOUSEBUTTONDOWN:  # Detects if the mouse button has been pressed
                if 550 <= mousePosition[0] <= 550 + 280:  # Detects if mouse position x is within set bounds
                    if 570 <= mousePosition[1] <= 570 + 80:  # Detects if mouse position y is within set bounds
                        print("Settings")  # This is where the code calling the settings menu

    # This next section of code relates to the play button detection of the mouse when hovered over
    if 550 <= mousePosition[0] <= 550 + 280:  # Detects if mouse position x is within set bounds
        if 270 <= mousePosition[1] <= 270 + 80:  # Detects if mouse position y is within set bounds
            pygame.draw.rect(MM, (170, 170, 170), [550, 270, 280, 80])  # Draws a lighter rectangle when hovered over

        else:
            pygame.draw.rect(MM, (100, 100, 100), [550, 270, 280, 80])  # Draws a darker rectangle when not hovered over
    else:
        pygame.draw.rect(MM, (100, 100, 100), [550, 270, 280, 80])  # Draws a darker rectangle when not hovered over

    # This next section of code relates to the shop menu button detection of the mouse when hovered over
    if 550 <= mousePosition[0] <= 550 + 280:  # Detects if mouse position x is within set bounds
        if 370 <= mousePosition[1] <= 370 + 80:  # Detects if mouse position y is within set bounds
            pygame.draw.rect(MM, (170, 170, 170), [550, 370, 280, 80])  # Draws a lighter rectangle when hovered over

        else:
            pygame.draw.rect(MM, (100, 100, 100), [550, 370, 280, 80])  # Draws a darker rectangle when not hovered over
    else:
        pygame.draw.rect(MM, (100, 100, 100), [550, 370, 280, 80])  # Draws a darker rectangle when not hovered over

    # This next section of code relates to the stats menu button detection of the mouse when hovered over
    if 550 <= mousePosition[0] <= 550 + 280:  # Detects if mouse position x is within set bounds
        if 470 <= mousePosition[1] <= 470 + 80:  # Detects if mouse position y is within set bounds
            pygame.draw.rect(MM, (170, 170, 170), [550, 470, 280, 80])  # Draws a lighter rectangle when hovered over

        else:
            pygame.draw.rect(MM, (100, 100, 100), [550, 470, 280, 80])  # Draws a darker rectangle when not hovered over
    else:
        pygame.draw.rect(MM, (100, 100, 100), [550, 470, 280, 80])  # Draws a darker rectangle when not hovered over

    # This next section of code relates to the setting menu button detection of the mouse when hovered over
    if 550 <= mousePosition[0] <= 550 + 280:  # Detects if mouse position x is within set bounds
        if 570 <= mousePosition[1] <= 570 + 80:  # Detects if mouse position y is within set bounds
            pygame.draw.rect(MM, (170, 170, 170), [550, 570, 280, 80])  # Draws a lighter rectangle when hovered over

        else:
            pygame.draw.rect(MM, (100, 100, 100), [550, 570, 280, 80])  # Draws a darker rectangle when not hovered over
    else:
        pygame.draw.rect(MM, (100, 100, 100), [550, 570, 280, 80])  # Draws a darker rectangle when not hovered over

    # This next section relates to the super imposing of text onto the buttons previously created
    MM.blit(startGameButton, (650, 290))  # Super imposes the start text on the start game button
    MM.blit(shopGameButton, (655, 385))  # Super imposes the shop text on the start game button
    MM.blit(statsGameButton, (650, 485))  # Super imposes the stats text on the start game button
    MM.blit(settingsGameButton, (625, 585))  # Super imposes the settings text on the start game button

    pygame.display.update()  # Updates the screen
