# Imports the libraries needed for the screen to work
import pygame

ScreenHeight = 1366  # Sets the screens height
ScreenWidth = 768  # Sets the screens width

# Setting up the pygame window
pygame.init()  # initializing the imported module
MM = pygame.display.set_mode((ScreenHeight, ScreenWidth))  # Displaying a window of set parameters

backGroundImage = pygame.image.load("Sprites/Background5.jpg").convert()  # Loading the background game sprite
backGroundPosition = 0  # Setting the backgrounds original position

# This section of the code creates fonts that can be used later
titleFont = pygame.font.SysFont('Comic Sans MS', 150)  # Sets the font and the size of font to be used for the title
textsurface = titleFont.render('Settings', False, (0, 0, 0))  # Sets the parameters for the title to be called later


class VolumeSlider:  # Creates the class used for the volume slider button
    def __init__(self, position_x, position_y, type):  # The simple base conditions
        self.PositionX = position_x
        self.PositionY = position_y
        self.Width = 100
        self.Height = 100
        self.Type = type
        self.CurrentMasterVolume = 100
        self.CurrentMusicVolume = 100

    @property
    def spawn(self):
        if self.CurrentMusicVolume >= 100 or self.CurrentMasterVolume >= 100:
            pygame.draw.rect(MM, (100, 100, 100), [900, self.PositionY, 50, 160])
            pygame.draw.rect(MM, (100, 100, 100), [800, self.PositionY + 20, 50, 140])
            pygame.draw.rect(MM, (100, 100, 100), [700, self.PositionY + 40, 50, 120])
            pygame.draw.rect(MM, (100, 100, 100), [600, self.PositionY + 60, 50, 100])
            pygame.draw.rect(MM, (100, 100, 100), [500, self.PositionY + 80, 50, 80])
            pygame.draw.rect(MM, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

        elif self.CurrentMusicVolume >= 80 or self.CurrentMasterVolume >= 80:
            pygame.draw.rect(MM, (100, 100, 100), [800, self.PositionY + 20, 50, 140])
            pygame.draw.rect(MM, (100, 100, 100), [700, self.PositionY + 40, 50, 120])
            pygame.draw.rect(MM, (100, 100, 100), [600, self.PositionY + 60, 50, 100])
            pygame.draw.rect(MM, (100, 100, 100), [500, self.PositionY + 80, 50, 80])
            pygame.draw.rect(MM, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

        elif self.CurrentMusicVolume >= 80 or self.CurrentMasterVolume >= 80:
            pygame.draw.rect(MM, (100, 100, 100), [700, self.PositionY + 40, 50, 120])
            pygame.draw.rect(MM, (100, 100, 100), [600, self.PositionY + 60, 50, 100])
            pygame.draw.rect(MM, (100, 100, 100), [500, self.PositionY + 80, 50, 80])
            pygame.draw.rect(MM, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

        elif self.CurrentMusicVolume >= 80 or self.CurrentMasterVolume >= 80:
            pygame.draw.rect(MM, (100, 100, 100), [600, self.PositionY + 60, 50, 100])
            pygame.draw.rect(MM, (100, 100, 100), [500, self.PositionY + 80, 50, 80])
            pygame.draw.rect(MM, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

        elif self.CurrentMusicVolume >= 80 or self.CurrentMasterVolume >= 80:
            pygame.draw.rect(MM, (100, 100, 100), [500, self.PositionY + 80, 50, 80])
            pygame.draw.rect(MM, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

        elif self.CurrentMusicVolume >= 80 or self.CurrentMasterVolume >= 80:
            pygame.draw.rect(MM, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

    def mechanics(self):
        if 1050 <= mousePosition[0] <= 1050 + 250:  # Detects if mouse position x is within set bounds
            if self.PositionY + 20 <= mousePosition[1] <= self.PositionY + 160:  # Detects if mouse position y is within set bounds
                pygame.draw.rect(MM, (80, 80, 80),
                                 [1050, self.PositionY + 10, 250, 140])  # Draws a lighter rectangle when hovered over

            else:
                pygame.draw.rect(MM, (0, 0, 0),
                                 [1050, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over
        else:
            pygame.draw.rect(MM, (0, 0, 0), [1050, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over

        if 50 <= mousePosition[0] <= 50 + 250:  # Detects if mouse position x is within set bounds
            if self.PositionY + 20 <= mousePosition[1] <= self.PositionY + 160:  # Detects if mouse position y is within set bounds
                pygame.draw.rect(MM, (80, 80, 80),
                                 [50, self.PositionY + 10, 250, 140])  # Draws a lighter rectangle when hovered over

            else:
                pygame.draw.rect(MM, (0, 0, 0),
                                 [50, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over
        else:
            pygame.draw.rect(MM, (0, 0, 0), [50, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over


MusicSlider = VolumeSlider(100, 200, "Music")
MasterSlider = VolumeSlider(100, 400, "Master")

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

    for event in pygame.event.get():  # Checks to see if any event in queue

        if event.type == pygame.QUIT:  # If event is quit
            running = False  # Set running bool to false

    MM.blit(textsurface, (375, -10))  # Displays stats screen title
    MusicSlider.spawn
    MusicSlider.mechanics()
    MasterSlider.spawn
    MasterSlider.mechanics()

    pygame.display.update()  # Updates the screen
