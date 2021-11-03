# Imports the libraries needed for the screen to work
import pygame

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

# Setting up the pygame window
pygame.init()  # initializing the imported module
MM = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters

backGroundImage = pygame.image.load("Sprites/Background5.jpg").convert()  # Loading the background game sprite
backGroundPosition = 0  # Setting the backgrounds original position

current_master_volume = 100
current_music_volume = 100

class VolumeSlider:  # Creates the class used for the volume slider button
    def __init__(self, position_x, position_y, type, current_master_volume, current_music_volume):  # The simple base conditions
        self.PositionX = position_x
        self.PositionY = position_y
        self.Width = 100
        self.Height = 100
        self.Type = type
        self.Current = current_master_volume
        self.CurrentMusicVolume = current_music_volume

    @property
    def spawn(self):
        if self.Type == "Music":
            if self.CurrentMusicVolume <= 100:
                return pygame.draw.rect(MM, (100, 100, 100), [550, 270, 80, 280]), pygame.draw.rect(MM, (100, 100, 100), [550, 270, 280, 80])

        else:
            return pygame.draw.rect(MM, (100, 100, 100), [550, 570, 280, 80])


MusicSlider = VolumeSlider(100, 100, "Music", current_master_volume, current_music_volume)
MasterSlider = VolumeSlider(100, 100, "Master", current_master_volume, current_music_volume)

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

    MusicSlider.spawn
    MasterSlider.spawn

    pygame.display.update()  # Updates the screen
