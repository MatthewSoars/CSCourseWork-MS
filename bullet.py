import pygame


# Code for the class of the bird sprite
class BulletClass(pygame.sprite.Sprite):
    def __init__(self, screen, pos_x, pos_y):  # Method called when class is instantiated
        pygame.sprite.Sprite.__init__(self)  # Inherits the parent Sprite class

        self.Screen = screen  # Sets the screen to add to
        self.PosX = pos_x  # Sets the x position
        self.PosY = pos_y  # Sets the y position

        self.bullet = pygame.Surface((30, 7))  # Creates the surface
        self.rect = self.bullet.get_rect()  # Sets the rect from the surface
        self.rect.y = pos_x  # Sets the rect y pos
        self.rect.x = pos_y  # Sets the rect x pos

        self.speed = 3  # Sets the speed
        self.rect.y += 50  # Sets the rect y
        self.rect.x += 10  # Sets the rect x

    def update(self, game_live):  # Method called to update the bullet class
        self.PosX = self.PosX + self.speed  # Moves the pos x depending on the speed
        self.rect.x = self.PosX  # Sets the rect pos x
        self.rect.y = self.PosY  # Sets the rect pos y

        # Draws the rect to the screen
        pygame.draw.rect(self.Screen, (0, 0, 0), (self.rect.x, self.rect.y, self.rect.width, self.rect.height))

        if self.rect.x < -400:  # If the rect pos x is less than - 400
            self.kill()  # Kills the sprite

        elif self.rect.x > 1600:  # If the rect pos x is more than 1600
            self.kill()  # Kills the sprite

        if not game_live:  # If the game is not live
            self.kill()  # Kills the sprite
