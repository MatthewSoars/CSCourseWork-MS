# Importing the required libraries
import pygame  # Imports the pygame library


# Code for the class of the tube
class TubeScoreLogic(pygame.sprite.Sprite):
    def __init__(self, screen):  # Method called when class is instantiated
        pygame.sprite.Sprite.__init__(self)  # Inherits the parent sprite class
        self.ScreenToAddTo = screen  # Sets the screen to add to
        self.speed = -3  # Sets the speed of the tube
        self.PosX = 1500 + 105  # Sets the Pos X of the tube

        self.tube_score = pygame.Surface((50, 768))  # Sets the surface for the tube score box
        self.rect = self.tube_score.get_rect()  # Sets the rect of the surface

        self.rect.y = 0  # Sets the y position of the rect
        self.rect.x = -400  # Sets the x position of the rect

    def update(self, game_live):  # Method to update the tube scoring box
        self.PosX += self.speed  # Moves the current position by the speed
        self.rect.x = self.PosX  # Sets the rect to the new position

        #  Draws the rect
        pygame.draw.rect(self.ScreenToAddTo, (0, 100, 0), (self.rect.x, self.rect.y, self.rect.width, self.rect.height))

        if self.rect.x < -400:  # If the position of x is less than -400
            self.kill()  # Kills the tube sprite

        elif not game_live:  # If the game is not live
            self.kill()  # Kills the tube sprite
