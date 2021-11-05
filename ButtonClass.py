import pygame


class Button:
    def __init__(self, position_y, position_x, width, height, text, mouse_pos_x, mouse_pos_y, screen):
        self.PosY = position_y
        self.PosX = position_x
        self.Length = width
        self.Height = height
        self.Text = text
        self.MouseX = mouse_pos_x
        self.MouseY = mouse_pos_y
        self.ScreenToAddTo = screen

    def refresh(self):
        # This next section of code relates to the setting menu button detection of the mouse when hovered over
        if self.PosX <= self.MouseX <= self.PosX + self.Length:  # Detects if mouse position x is within set bounds
            if self.PosY <= self.MouseY <= self.PosY + self.Height:  # Detects if mouse position y is within set bounds
                pygame.draw.rect(self.ScreenToAddTo, (170, 170, 170),
                                 [self.PosX, self.PosY, self.Length,
                                  self.Height])  # Draws a lighter rectangle when hovered over

            else:
                pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100),
                                 [550, 570, 280, 80])  # Darker rectangle when not hovered over
        else:
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100),
                             [550, 570, 280, 80])  # Draws a darker rectangle when not hovered over

    def button_press_checker(self):
        pass
