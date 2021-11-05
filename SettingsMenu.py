# Imports the libraries needed for the screen to work
import pygame
from VolumeSliderClass import VolumeSlider

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

music_volume = 0
master_volume = 0

# Setting up the pygame window
pygame.init()  # initializing the imported module
MM = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters

backGroundImage = pygame.image.load("Sprites/Background5.jpg").convert()  # Loading the background game sprite
backGroundPosition = 0  # Setting the backgrounds original position

# This section of the code creates fonts that can be used later
titleFont = pygame.font.SysFont('Comic Sans MS', 150)  # Sets the font and the size of font to be used for the title
textsurface = titleFont.render('Settings', False, (0, 0, 0))  # Sets the parameters for the title to be called later

MusicSlider = VolumeSlider(200, "Music", MM, music_volume, master_volume)
MasterSlider = VolumeSlider(400, "Master", MM, music_volume, master_volume)

running = True  # Sets the running boolean to true
# Game loop while the program is running
while running:
    mouse_position = pygame.mouse.get_pos()  # Gets the current position of the mouse and stores it
    mouse_position_x = mouse_position[0]
    mouse_position_y = mouse_position[1]

    # This section of code uses two backgrounds to create an infinite effect
    relativeBackGroundPosition = backGroundPosition % backGroundImage.get_rect().width  # Uses mod to move background
    MM.blit(backGroundImage, (relativeBackGroundPosition - backGroundImage.get_rect().width, 0))  # Blits the background
    if relativeBackGroundPosition < ScreenHeight:  # When relativeBackGroundPosition is more then ScreenHeight
        MM.blit(backGroundImage, (relativeBackGroundPosition, 0))  # Blits the second background image to the screen
    backGroundPosition -= 1  # Makes the background shift to the left

    MM.blit(textsurface, (375, -10))  # Displays stats screen title

    MusicSlider.hover(mouse_position_x, mouse_position_y)
    MusicSlider.refresh(music_volume, master_volume)
    MasterSlider.hover(mouse_position_x, mouse_position_y)
    MasterSlider.refresh(music_volume, master_volume)

    for event in pygame.event.get():  # Checks to see if any event in queue

        if event.type == pygame.QUIT:  # If event is quit
            running = False  # Set running bool to false

        elif event.type == pygame.MOUSEBUTTONDOWN:
            music_volume = MusicSlider.button_press_checker(music_volume, mouse_position_x, mouse_position_y)
            master_volume = MasterSlider.button_press_checker(master_volume, mouse_position_x, mouse_position_y)

    pygame.display.update()  # Updates the screen
