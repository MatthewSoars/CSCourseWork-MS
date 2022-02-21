# Imports the libraries needed for the screen to work
import pygame  # Imports the pygame library

# Code for the class of the music logic
class LogicMusic:
    def __init__(self):  # Function when class is instantiated
        list_of_music = ["Sounds/Music/Figure It Out - 8bit - Royal Blood (320 kbps).mp3"]  # List of music to play
        for music in list_of_music:  # For the number of items within the list previously created
            pygame.mixer.music.load(music)  # Loads all the music in the list
        pygame.mixer.music.play(-1)  # Loops the music forever

    @staticmethod
    def volume_change(new_volume):  # Method to change the volume of the music
        pygame.mixer.music.set_volume(new_volume) # Changes volume from 0 - 1
