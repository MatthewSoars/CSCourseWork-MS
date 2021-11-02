# Imports the libraries needed for the screen to work
import pygame

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

# Setting up the pygame window
pygame.init()  # initializing the imported module
MM = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters

backGroundImage = pygame.image.load("Sprites/Background5.jpg").convert()  # Loading the background game sprite
backGroundPosition = 0  # Setting the backgrounds original position


class VolumeSlider:  # Creates the class used for the volume slider button
    def __init__(self, position_x, position_y):  # The simple base conditions for the visible section
        self.PositionX = position_x
        self.PositionY = position_y

    def sound_up(self, controling, current_music_volume, current_master_volume):
        if controling:
            current_music_volume = current_music_volume + 1

    def sound_down(self):
        soundDown = True


running = True  # Sets the running boolean to true
# Game loop while the program is running
while running:

    # This section of code uses two backgrounds to create an infinite effect
    relativeBackGroundPosition = backGroundPosition % backGroundImage.get_rect().width  # Uses mod to move background
    MM.blit(backGroundImage, (relativeBackGroundPosition - backGroundImage.get_rect().width, 0))  # Blits the background
    if relativeBackGroundPosition < ScreenHeight:  # When relativeBackGroundPosition is more then ScreenHeight
        MM.blit(backGroundImage, (relativeBackGroundPosition, 0))  # Blits the second background image to the screen
    backGroundPosition -= 1  # Makes the background shift to the left

    for event in pygame.event.get():  # Checks to see if any event in queue

        if event.type == pygame.QUIT:  # If event is quit
            running = False  # Set running bool to false

    pygame.display.update()  # Updates the screen
