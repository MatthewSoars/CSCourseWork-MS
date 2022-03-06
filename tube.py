# Importing the required libraries
import pygame  # Imports the pygame library


# Code for the class of the tube
class TubeLogic(pygame.sprite.Sprite):
    def __init__(self, screen, top, gap_pos):  # Method called when class is instantiated
        pygame.sprite.Sprite.__init__(self)  # Method called when class is instantiated
        self.ScreenToAddTo = screen  # Setting the screen to add to
        self.GapSize = 300  # Setting the gap size
        self.speed = -3  # Sets the speed of the tube
        self.PosX = 1500  # Sets the starting X position

        self.GapPos = gap_pos  # Sets the gap pos
        self.Top = top  # Sets if the tube is the top one or not

        height_calc = (768 / 2) - (self.GapSize / 2)  # Calculates the height of the tube

        if self.Top:  # If the tube is a top one
            self.top_tube = pygame.Surface((250, height_calc + self.GapPos))  # Creates the surface
            self.top_rect = self.top_tube.get_rect()  # Sets the rect from the surface
            self.top_tube.fill((0, 100, 0))  # Fills the rectangle
            self.rect = self.top_rect  # Sets the rect for the sprite to work
            self.rect.y = 0  # Sets the rect y pos
            self.rect.x = 1000  # Sets the rect x pos

        elif not self.Top:  # If the tube is a bottom one
            self.bottom_tube = pygame.Surface((250, height_calc + self.GapPos + 500))  # Creates the surface
            self.bottom_rect = self.bottom_tube.get_rect()  # Sets the rect from the surface
            self.bottom_tube.fill((0, 100, 0))  # Fills the rectangle
            self.rect = self.bottom_rect  # Sets the rect for the sprite to work
            self.rect.y = 768 - (height_calc - self.GapPos)  # Sets the rect y pos
            self.rect.x = 1000  # Sets the rect x pos

    def update(self, game_live):  # Method to update the tube sprite
        self.PosX = self.PosX + self.speed  # Moves the pos x depending on the speed
        self.rect.x = self.PosX  # Sets the rect pos x

        # Draws the rect to the screen
        pygame.draw.rect(self.ScreenToAddTo, (0, 100, 0), (self.rect.x, self.rect.y, self.rect.width, self.rect.height))

        if self.rect.x < -400:  # If the rect pos x is less than - 400
            self.kill()  # Kills the sprite

        if not game_live:  # If the game is not live
            self.kill()  # Kills the sprite
