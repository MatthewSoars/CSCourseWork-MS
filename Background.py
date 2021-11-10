# Importing the libraries need for the parallax effect to work
import pygame

class ParallaxEffect:
    def __init__(self):


    def parallax_effect(screen, back_ground_position, back_ground_image, screen_height):
        # This section of code uses two backgrounds to create an infinite effect
        relativeBackGroundPosition = back_ground_position % back_ground_image.get_rect().width  # Uses mod to move background
        screen.blit(back_ground_image, (relativeBackGroundPosition - back_ground_image.get_rect().width, 0))  # Blits the background
        if relativeBackGroundPosition < screen_height:  # When relativeBackGroundPosition is more then ScreenHeight
            screen.blit(back_ground_image, (relativeBackGroundPosition, 0))  # Blits the second background image to the screen
        back_ground_position -= 2  # Makes the background shift to the left
        print("Yea")

