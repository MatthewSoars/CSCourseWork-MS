import pygame


# Code for the class of the bird sprite
class BirdClass:
    def __init__(self, screen):  # Method called when class is instantiated
        self.ScreenToAddTo = screen  # Gets the screen that is needed to be added to
        self.Jump_Height = 2  # Sets the jump height of the bird
        self.Current_Skin = 1  # Sets the starting skin of the bird
        self.ScreenPosX = 150  # Sets the stating X position
        self.ScreenPosY = 0  # Sets the starting Y position
        self.Gravity = -2  # Sets the gravity that the bird abides by
        self.Sprite = pygame.image.load("Sprites/BirdSprite/StandardBird/frame-1.png").convert()  # Sets Image of sprite
        self.Sprite.set_colorkey((18, 255, 0))  # Sets the background colour to be taken out
        self.Sprite = pygame.transform.scale(self.Sprite, (200, 150))  # Scales the image to the size needed
        self.FlyCoolDown = 60  # Sets the time needed between presses of the fly button
        self.Acceleration = 0  # Sets the starting acceleration

        self.hit_box = self.Sprite.get_rect()  # Defines the rectangular hit box of a sprite
        self.radius = int(self.hit_box.width * 1.20)  # Defines the circle hit box for the sprite
        self.hit_box.x = self.ScreenPosX + 25  # Sets the x position of the hit box
        self.hit_box.y = self.ScreenPosY + 20  # Sets the y position of the hit box
        # pygame.draw.circle(self.Sprite, (255, 0, 0), self.hit_box.center, self.radius)

    def Update(self, game_state):  # Method called to update the bird sprite

        if self.Acceleration < 10:  # If Acceleration is less than 10
            self.Acceleration += 1  # Acceleration incremented by 1

        self.ScreenPosY += self.Acceleration  # Calculates the effect the acceleration has
        self.hit_box.y += self.Acceleration  # Moves the hit box with the sprite

        angle = self.Acceleration * -3  # Calculates the angle for sprite based on acceleration
        rotated_sprite = pygame.transform.rotate(self.Sprite, angle)  # Sets the amount to rotate the sprite

        self.ScreenToAddTo.blit(rotated_sprite, (self.ScreenPosX, self.ScreenPosY))  # Blitz the changes to the screen

    def AutoFly(self):  # Auto fly method to be used within the menu
        if self.ScreenPosY >= 360:  # If the spite fulls below a certain threshold in the Y axis
            self.Acceleration = -20  # Sprite counteracts the full by using acceleration

    def ShopScreen(self):  # Method used within the shop screen menu
        self.ScreenToAddTo.blit(self.Sprite, (575, 300))  # Sets the position used in the menu

    def Fly(self):  # Method that is assigned to a key press which accelerates the sprite up
        self.Acceleration = -25  # Sprite counteracts the fall by using acceleration

    def SkinChanger(self, direction_of_change):  # Skin changer method
        self.Current_Skin += direction_of_change
        if self.Current_Skin >= 0:
            self.Current_Skin = 1

