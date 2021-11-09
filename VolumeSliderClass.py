import pygame


class VolumeSlider:  # Creates the class used for the volume slider button
    def __init__(self, position_y, type, screen):  # The simple base conditions
        self.PositionY = position_y
        self.Width = 100
        self.Height = 100
        self.Type = type
        self.ScreenToAddTo = screen

    def hover(self, mouse_position):
        if 1050 <= mouse_position[0] <= 1050 + 250:  # Detects if mouse position x is within set bounds
            if self.PositionY + 20 <= mouse_position[1] <= self.PositionY + 160:  # Detects if mouse y is in bounds
                pygame.draw.rect(self.ScreenToAddTo, (80, 80, 80),
                                 [1050, self.PositionY + 10, 250, 140])  # Draws a lighter rectangle when hovered over

            else:
                pygame.draw.rect(self.ScreenToAddTo, (0, 0, 0),
                                 [1050, self.PositionY + 10, 250,
                                  140])  # Draws a darker rectangle when not hovered over
        else:
            pygame.draw.rect(self.ScreenToAddTo, (0, 0, 0),
                             [1050, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over

        if 50 <= mouse_position[0] <= 50 + 250:  # Detects if mouse position x is within set bounds
            if self.PositionY + 20 <= mouse_position[1] <= self.PositionY + 160:  # Detects if mouse y is in bounds
                pygame.draw.rect(self.ScreenToAddTo, (80, 80, 80),
                                 [50, self.PositionY + 10, 250, 140])  # Draws a lighter rectangle when hovered over

            else:
                pygame.draw.rect(self.ScreenToAddTo, (0, 0, 0),
                                 [50, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over
        else:
            pygame.draw.rect(self.ScreenToAddTo, (0, 0, 0),
                             [50, self.PositionY + 10, 250, 140])  # Draws a darker rectangle when not hovered over

    def button_press_checker(self, volume, mouse_position):
        if 1050 <= mouse_position[0] <= 1050 + 250:  # Detects if mouse position x is within set bounds
            if self.PositionY <= mouse_position[1] <= self.PositionY + 160 and volume < 100:  # Detects if mouse y
                if self.Type == "Music":
                    volume = volume + 20
                    return volume

                elif self.Type == "Master":
                    volume = volume + 20
                    return volume

        if 50 <= mouse_position[0] <= 50 + 250:  # Detects if mouse position x is within set bounds
            if self.PositionY <= mouse_position[1] <= self.PositionY + 160 and volume > 0:  # Detects if mouse y
                if self.Type == "Music":
                    volume = volume - 20
                    return volume

                elif self.Type == "Master":
                    volume = volume - 20
                    return volume
            else:
                return volume

        else:
            return volume

    def refresh(self, music_volume, master_volume):
        if music_volume == 100 and self.Type == "Music" or master_volume == 100 and self.Type == "Master":
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [850, self.PositionY, 50, 160])
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [750, self.PositionY + 20, 50, 140])
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [650, self.PositionY + 40, 50, 120])
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [550, self.PositionY + 60, 50, 100])
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [450, self.PositionY + 80, 50, 80])

        elif music_volume == 80 and self.Type == "Music" or master_volume == 80 and self.Type == "Master":
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [750, self.PositionY + 20, 50, 140])
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [650, self.PositionY + 40, 50, 120])
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [550, self.PositionY + 60, 50, 100])
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [450, self.PositionY + 80, 50, 80])

        elif music_volume == 60 and self.Type == "Music" or master_volume == 60 and self.Type == "Master":
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [650, self.PositionY + 40, 50, 120])
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [550, self.PositionY + 60, 50, 100])
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [450, self.PositionY + 80, 50, 80])

        elif music_volume == 40 and self.Type == "Music" or master_volume == 40 and self.Type == "Master":
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [550, self.PositionY + 60, 50, 100])
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 0), [450, self.PositionY + 80, 50, 80])

        elif music_volume == 20 and self.Type == "Music" or master_volume == 20 and self.Type == "Master":
            pygame.draw.rect(self.ScreenToAddTo, (255, 0, 00), [450, self.PositionY + 80, 50, 80])

        elif music_volume == 0 and self.Type == "Music" or master_volume == 0 and self.Type == "Master":
            mute_font = pygame.font.SysFont('Comic Sans MS', 120)  # Sets the font and size of font used for mute text
            mute_text = mute_font.render('Mute', False, (255, 0, 0))  # Sets mute text parameters
            self.ScreenToAddTo.blit(mute_text, (550, self.PositionY - 20))  # Displays stats screen title
