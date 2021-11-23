# Imports the libraries needed for the screen to work
import pygame  # Imports the pygame library


# Code for the class of the Button
class Button:
    def __init__(self, position_x, position_y, width, height, text, screen):  # Function when class is instantiated
        self.PosY = position_y  # Sets the position for the x coordinate
        self.PosX = position_x  # Sets the position for the y coordinate
        self.Length = width  # Sets the width of the button
        self.Height = height  # Sets the height of the button
        self.Text = text  # Sets the text stated within the button
        self.ScreenToAddTo = screen  # Screen that the button is needed to be added to

    # Function that is called to refresh the button object
    def refresh(self, mouse_position):
        # This next section of code relates to the setting menu button detection of the mouse when hovered over
        if self.PosX <= mouse_position[0] <= self.PosX + self.Length:  # If mouse position x is within set bounds
            if self.PosY <= mouse_position[1] <= self.PosY + self.Height:  # If mouse position y is within set bounds
                pygame.draw.rect(self.ScreenToAddTo, (170, 170, 170),
                                 [self.PosX, self.PosY, self.Length,
                                  self.Height])  # Draws a lighter rectangle when hovered over

            else:
                pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100),
                                 [self.PosX, self.PosY, self.Length, self.Height])  # Draws a darker rectangle
        else:
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100),
                             [self.PosX, self.PosY, self.Length, self.Height])  # Draws a darker rectangle

        TextLength = len(self.Text)  # Sets the length of the text variable
        buttonFont = pygame.font.SysFont('Comic Sans MS', 35)  # Sets the font and the size of font
        ButtonType = buttonFont.render(self.Text, True, (0, 0, 0))  # Sets parameters for the button to be used later
        self.ScreenToAddTo.blit(ButtonType, (self.PosX + (self.Length / 2) - (TextLength * 9),
                                             self.PosY + (self.Height / 4)))  # Super imposes the text on the button

    # Function called to check if the button has been changed
    def button_press_checker(self, mouse_position):
        if self.PosX <= mouse_position[0] <= self.PosX + self.Length:  # Detects mouse x is within set bounds
            if self.PosY <= mouse_position[1] <= self.PosY + self.Height:  # Detects mouse x is within set bounds
                return "Stats"  # This is where the type selected is returned
