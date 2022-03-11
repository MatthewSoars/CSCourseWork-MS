# Importing the required libraries
import pygame  # Imports the pygame library
import random  # Import the random library


# Code for the class of the tube
class WallLogic(pygame.sprite.Sprite):
    def __init__(self, screen, pos_x, pos_y):  # Method called when class is instantiated
        pygame.sprite.Sprite.__init__(self)  # Method called when class is instantiated
        self.ScreenToAddTo = screen  # Setting the screen to add to
        self.speed = -5  # Sets the speed of the tube

        self.PosX = pos_x  # Sets the starting X position
        self.PosY = pos_y  # Sets the starting Y position

        self.Height = random.randint(70, 200)  # Sets a random height for the wall

        self.Wall = pygame.Surface((50, self.Height))  # Creates the surface
        self.rect = self.Wall.get_rect()  # Sets the rect from the surface
        self.rect.width = 50
        self.rect.height = self.Height

    def update(self, game_live):  # Method to update the tube sprite
        self.PosX = self.PosX + self.speed  # Moves the pos x depending on the speed
        self.rect.x = self.PosX  # Sets the rect pos x
        self.rect.y = self.PosY

        # Draws the rect to the screen
        pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), (self.rect.x, self.PosY, self.rect.width, self.rect.height))

        if self.rect.x < -400:  # If the rect pos x is less than - 400
            self.kill()  # Kills the sprite

        if not game_live:  # If the game is not live
            self.kill()  # Kills the sprite
