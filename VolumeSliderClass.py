import pygame

class VolumeSlider:  # Creates the class used for the volume slider button
    def __init__(self, position_x, position_y, type, screen, mouse_pos_x, mouse_pos_y):  # The simple base conditions
        self.PositionX = position_x
        self.PositionY = position_y
        self.Width = 100
        self.Height = 100
        self.Type = type
        self.CurrentMasterVolume = 100
        self.CurrentMusicVolume = 100
        self.ScreenToAddTo = screen
        self.MousePositionX = mouse_pos_x
        self.MousePositionY = mouse_pos_y

    def spawn(self):
        if self.CurrentMusicVolume >= 100 or self.CurrentMasterVolume >= 100:
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [900, self.PositionY, 50, 160])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [800, self.PositionY + 20, 50, 140])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [700, self.PositionY + 40, 50, 120])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [600, self.PositionY + 60, 50, 100])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [500, self.PositionY + 80, 50, 80])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

        elif self.CurrentMusicVolume >= 80 or self.CurrentMasterVolume >= 80:
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [800, self.PositionY + 20, 50, 140])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [700, self.PositionY + 40, 50, 120])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [600, self.PositionY + 60, 50, 100])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [500, self.PositionY + 80, 50, 80])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

        elif self.CurrentMusicVolume >= 80 or self.CurrentMasterVolume >= 80:
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [700, self.PositionY + 40, 50, 120])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [600, self.PositionY + 60, 50, 100])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [500, self.PositionY + 80, 50, 80])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

        elif self.CurrentMusicVolume >= 80 or self.CurrentMasterVolume >= 80:
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [600, self.PositionY + 60, 50, 100])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [500, self.PositionY + 80, 50, 80])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

        elif self.CurrentMusicVolume >= 80 or self.CurrentMasterVolume >= 80:
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [500, self.PositionY + 80, 50, 80])
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

        elif self.CurrentMusicVolume >= 80 or self.CurrentMasterVolume >= 80:
            pygame.draw.rect(self.ScreenToAddTo, (100, 100, 100), [400, self.PositionY + 100, 50, 60])

    def mechanics(self):
        if 1050 <= self.MousePositionX <= 1050 + 250:  # Detects if mouse position x is within set bounds
            if self.PositionY + 20 <= self.MousePositionY <= self.PositionY + 160:  # Detects if mouse position y is within set bounds
                pygame.draw.rect(self.ScreenToAddTo, (80, 80, 80),
                                 [1050, self.PositionY + 10, 250, 140])  # Draws a lighter rectangle when hovered over

            else:
                pygame.draw.rect(self.ScreenToAddTo, (0, 0, 0),
                                 [1050, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over
        else:
            pygame.draw.rect(self.ScreenToAddTo, (0, 0, 0), [1050, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over

        if 50 <= self.MousePositionX <= 50 + 250:  # Detects if mouse position x is within set bounds
            if self.PositionY + 20 <= self.MousePositionY <= self.PositionY + 160:  # Detects if mouse position y is within set bounds
                pygame.draw.rect(self.ScreenToAddTo, (80, 80, 80),
                                 [50, self.PositionY + 10, 250, 140])  # Draws a lighter rectangle when hovered over

            else:
                pygame.draw.rect(self.ScreenToAddTo, (0, 0, 0),
                                 [50, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over
        else:
            pygame.draw.rect(self.ScreenToAddTo, (0, 0, 0), [50, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over