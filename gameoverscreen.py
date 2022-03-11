# Importing the needed libraries
import pygame  # Importing pygame
from ButtonClass import Button  # Imports the button class
import shelve  # Imports the shelve library


class GameOverScreenLogic:
    def __init__(self, screen, score):  # Method called when class is instantiated
        self.ScreenToAddTo = screen  # Sets the screen to add too

        self.GameOverScreen = pygame.Surface((900, 600))  # Sets the pygame surface area
        self.rect = self.GameOverScreen.get_rect()  # Defines the rect
        self.rect.y = 30  # Sets the rect y pos
        self.rect.x = 250  # Sets the rect x pos

        self.Score = "Score = " + str(score)  # Sets the score with the text
        self.High_Score = "High Score ="  # Sets an initial high score

        self.DeathMSG = "Don't Fly Low Next Time"  # Sets the death MSG

        # This section of the code instantiates the buttons
        self.PlayAgainButton = Button(350, 450, 280, 80, "Play Again",
                                      self.ScreenToAddTo)  # Sets parameters for the exit button
        self.ExitButton = Button(750, 450, 280, 80, "Exit", self.ScreenToAddTo)  # Sets parameters for the exit button

        # This section of the code creates fonts that can be used later
        game_over_font = pygame.font.SysFont('Comic Sans MS', 170)  # Sets the font and the size of font
        death_msg_font = pygame.font.SysFont('Comic Sans MS', 70)  # Sets the font and the size of font
        self.score_font = pygame.font.SysFont('Comic Sans MS', 60)  # Sets the font and the size of font
        self.game_over_text = game_over_font.render('Game Over', False, (0, 0, 0))  # Sets the parameters for the Game over text
        self.death_msg_text = death_msg_font.render(self.DeathMSG, False, (0, 0, 0))  # Sets the parameters for the death msg

    # Method called to update the game over screen
    def update(self, score, distance_traveled):
        # Section of the code which relates to the handling of the updating of high score txt document
        txt_doc = shelve.open('scores.txt')  # Opens the score txt
        high_score = txt_doc['score']  # Score is read from the disk
        distance = txt_doc['distance']  # Distance is read from the disk
        if high_score < score:  # If previous score is more than high score
            txt_doc['score'] = score  # New high score is saved to disk
        distance += distance_traveled  # Adds distance to distance traveled
        txt_doc['distance'] = distance  # New distance is saved to disk
        txt_doc.close()  # Closes the txt file

        self.Score = "Score = " + str(score)  # Sets the score with the text
        self.High_Score = "High Score = " + str(high_score)  # Sets the high score with the text

        score_text = self.score_font.render(self.Score, False, (0, 0, 0))  # Sets the parameters for the score msg text
        high_score_text = self.score_font.render(self.High_Score, False, (0, 0, 0))  # Sets the parameters for the score msg text

        mouse_position = pygame.mouse.get_pos()  # Gets the current position of the mouse and stores it

        pygame.draw.rect(self.ScreenToAddTo, (0, 100, 0),
                         pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height), 500,
                         50)  # Draws Rect With Curved Edges

        self.ScreenToAddTo.blit(self.game_over_text, (265, 30))  # Displays the game over text to the screen
        self.ScreenToAddTo.blit(self.death_msg_text, (290, 230))  # Displays the game over text to the screen
        self.ScreenToAddTo.blit(score_text, (350, 340))  # Displays the game over text to the screen
        self.ScreenToAddTo.blit(high_score_text, (700, 340))  # Displays the game over text to the screen

        self.PlayAgainButton.refresh(mouse_position)  # Instantiates a play again button
        self.ExitButton.refresh(mouse_position)  # Instantiates an exit button

    def game_state_change(self, mouse_position):  # Method to change the game state
        game_state = 'GameMenu'  # Sets the game state
        restart = False  # Sets restart to False

        if self.PlayAgainButton.button_press_checker(mouse_position):  # If start button is pressed
            game_state = "GameMenu"  # Sets the game state
            restart = True  # Sets restart to True

        elif self.ExitButton.button_press_checker(mouse_position):  # If shop button is pressed
            game_state = "MainMenu"  # Sets the game state to 'ShopMenu'
            restart = True  # Sets restart to True

        return game_state, restart  # Returns the game_state
