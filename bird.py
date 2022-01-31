import pygame


# Code for the class of the bird sprite
class BirdClass:
    def __init__(self, screen):  # Method called when class is instantiated
        self.ScreenToAddTo = screen  # Gets the screen that is needed to be added to
        self.Jump_Height = 50  # Sets the jump height of the bird
        self.Current_Skin = 1  # Sets the starting skin of the bird
        self.ScreenPosX = 150  # Sets the stating X position
        self.ScreenPosY = 0  # Sets the starting Y position
        self.Gravity = -2  # Sets the gravity that the bird abides by
        self.Image = pygame.image.load("Sprites/BirdSprite/StandardBird/frame-1.png").convert()  # Sets Image of sprite
        self.Image.set_colorkey((18, 255, 0))  # Sets the background colour to be taken out
        self.Image = pygame.transform.scale(self.Image, (200, 150))  # Scales the image to the size needed
        self.FlyCoolDown = 60  # Sets the time needed between presses of the fly button
        self.Acceleration = 0  # Sets the starting acceleration

    def Update(self):  # Method called to update the bird sprite
        if self.Acceleration < 10:  # If Acceleration is less than 10
            self.Acceleration += 1  # Acceleration incremented by 1
        # Future angle calculation to go here
        self.ScreenPosY += self.Acceleration  # Calculates the effect the acceleration has
        self.ScreenToAddTo.blit(self.Image, (self.ScreenPosX, self.ScreenPosY))  # Blitz the changes to the screen

    def AutoFly(self):  # Auto fly method to be used within the menu
        if self.ScreenPosY >= 400:  # If the spite fulls below a certain threshold in the Y axis
            self.Acceleration = -25  # Sprite counteracts the full by using accelration

    def ShopScreen(self):  # Method used within the shop screen menu
        self.ScreenToAddTo.blit(self.Image, (575, 300))  # Sets the position used

    def SkinChanger(self, direction_of_change):  # Skin changer method
        self.Current_Skin += direction_of_change
        if self.Current_Skin >= 0:
                pass
