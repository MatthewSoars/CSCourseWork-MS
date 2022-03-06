# Importing the required libraries
import pygame


# Code for the class of the tube
class FloorHitBoxLogic(pygame.sprite.Sprite):
    def __init__(self, screen):  # Method called when class is instantiated
        pygame.sprite.Sprite.__init__(self)  # Call to the parent class of sprite
        self.ScreenToAddTo = screen  # Sets the screen to add to

        self.tube_score = pygame.Surface((1365, 1))  # Defines the pygame surface
        self.rect = self.tube_score.get_rect()  # Defines the rect
        self.rect.y = 770  # Sets the rect y pos
