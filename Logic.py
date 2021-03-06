# Imports the libraries needed for the screen to work
import pygame  # Imports the pygame library


class LogicBackground:
    def __init__(self):  # Function when class is instantiated
        self.back_ground_image = pygame.image.load("Sprites/Background5.jpg").convert()  # Loading the background
        self.back_ground_position = 0  # Setting the backgrounds original position

    def refresh(self, screen, screen_height):
        # This section of code uses two backgrounds to create an infinite effect (Uses MOD to move the background)
        relative_back_ground_position = self.back_ground_position % self.back_ground_image.get_rect().width  # Uses MOD
        screen.blit(self.back_ground_image, (
            relative_back_ground_position - self.back_ground_image.get_rect().width, 0))  # Adds the background

        if relative_back_ground_position < screen_height:  # When relativeBackGroundPosition is more than ScreenHeight
            screen.blit(self.back_ground_image,
                        (relative_back_ground_position, 0))  # Adds the second background image to the screen

        self.back_ground_position -= 3  # Makes the background shift to the left
