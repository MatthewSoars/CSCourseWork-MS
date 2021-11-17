import pygame


class LogicBackground:
    def __init__(self):
        self.back_ground_image = pygame.image.load("Sprites/Background5.jpg").convert()  # Loading the background
        self.back_ground_position = 0  # Setting the backgrounds original position

    def refresh(self, screen, screen_height):
        # This section of code uses two backgrounds to create an infinite effect
        relativeBackGroundPosition = self.back_ground_position % self.back_ground_image.get_rect().width  # Uses mod to move background
        screen.blit(self.back_ground_image, (
            relativeBackGroundPosition - self.back_ground_image.get_rect().width, 0))  # Blits the background

        if relativeBackGroundPosition < screen_height:  # When relativeBackGroundPosition is more then ScreenHeight
            screen.blit(self.back_ground_image,
                             (relativeBackGroundPosition, 0))  # Blits the second background image to the screen

        self.back_ground_position -= 3  # Makes the background shift to the left
