# importing the required libraries
import pygame  # Importing pygame
import random  # Importing random
from tube import TubeLogic  # Importing the tube class
from scorebox import TubeScoreLogic  # Importing the score class
from floorhitbox import FloorHitBoxLogic  # Importing the floor hit box class
from gameoverscreen import GameOverScreenLogic  # Importing the game over screen class


# Code for the class of the bird sprite
class LogicGameMenu:
    def __init__(self, screen, all_sprite_group, mob_group,
                 tube_hit_box_group, bullet_group, wall_group):  # Method called when class is instantiated
        self.ScreenToAddTo = screen  # Sets the screen to add sprites to
        self.SpriteGroup = all_sprite_group  # Sets the sprite group within the class
        self.MobGroup = mob_group  # Sets the sprite group within the class
        self.TubeHitBoxGroup = tube_hit_box_group  # Sets the sprite group within the class
        self.BulletGroup = bullet_group  # Sets the bullet group
        self.WallGroup = wall_group  # Sets the wall group

        self.RandomGap = 100  # sets the initial gap size
        self.Gap = 0  # Sets another initial value for gap size

        self.CurrentScore = 0  # sets the initial current score
        self.GameLive = True  # sets the game to live

        self.text_font = pygame.font.SysFont('Comic Sans MS', 35)  # Sets the font and the size of font

        self.FloorHitBoxGroup = pygame.sprite.Group()  # Creates a sprite group for the floor hit box
        self.floor_box = FloorHitBoxLogic(self.ScreenToAddTo)  # Instantiates the floor hit box
        self.FloorHitBoxGroup.add(self.floor_box)  # Adds the sprite to the group

        self.GameOverScreen = 0  # Creates the game over screen class variable
        self.game_over_screen_init = False  # Sets the game over screen to false

        self.crash_sound = pygame.mixer.Sound("Sounds/SoundEffects/hit.mp3")   # Sets the crash sound to the needed audio
        self.point_sound = pygame.mixer.Sound("Sounds/SoundEffects/point.mp3")  # Sets the point sound to the needed audio
        self.explosion_sound = pygame.mixer.Sound("Sounds/SoundEffects/explosion.mp3")  # Sets the explosion sound

        self.Distance_Traveled = 0  # Sets the initial distance travelled

        self.death_text = "You died"  # Sets the default death text

    def refresh(self, game_state, player_sprite, mob_sprites):  # refresh method which is called to refresh the screen
        self.Distance_Traveled += 1  # Increments distance traveled

        if self.GameLive:  # If the game is live
            if self.Gap >= self.RandomGap:  # If the Gap currently created is more than or equal to random gap size
                LogicGameMenu.Tube_Spawn(self)  # Spawns the tube to the screen
                LogicGameMenu.TimerStart(self)  # Starts the timer to spawn the next tube

            elif self.Gap < self.RandomGap:  # If the tube gap is less than the random gap
                self.Gap += 1  # increments the gap

            # Handles The Collisions of the sprites
            if game_state == "GameMenu":  # If game state  is GameMenu
                hit_tube = pygame.sprite.spritecollide(player_sprite, mob_sprites, False)  # If Player and Mob collide
                hit_hit_box = pygame.sprite.spritecollide(player_sprite, self.TubeHitBoxGroup, True)  # If player and Tube hit box collide
                hit_floor = pygame.sprite.spritecollide(player_sprite, self.FloorHitBoxGroup, False)  # If player and floor hit box collide
                hit_bullet_wall = pygame.sprite.groupcollide(self.BulletGroup, self.WallGroup, True, True)  # If Player and Mob collide
                hit_sprite_wall = pygame.sprite.spritecollide(player_sprite, self.WallGroup, False)
                if hit_tube:  # If hit tube is True
                    self.death_text = "Avoid the tube next time"  # Death text
                    self.GameLive = False  # Set game live to False
                    pygame.mixer.Sound.play(self.crash_sound)  # Plays the crash sound

                if hit_hit_box:  # If the score hit box is True
                    self.CurrentScore += 1  # Increment the current score
                    pygame.mixer.Sound.play(self.point_sound)  # Plays the point sound

                if hit_floor:  # If the hit floor box is True
                    self.death_text = "Don't fly too low next time"  # Death text
                    self.GameLive = False  # Sets the game live to False
                    pygame.mixer.Sound.play(self.crash_sound)  # Plays the crash sound

                if hit_sprite_wall:  # If the sprite hits the wall
                    self.death_text = "Avoid the wall next time"  # Death text
                    self.GameLive = False
                    pygame.mixer.Sound.play(self.crash_sound)  # Plays the crash sound

                if hit_bullet_wall:  # If the bullet hits the wall
                    pygame.mixer.Sound.play(self.explosion_sound)  # Plays the explosion sound

        elif not self.GameLive:  # If game live is False
            if not self.game_over_screen_init:  # If game over screen initialised is False
                self.GameOverScreen = GameOverScreenLogic(self.ScreenToAddTo, self.CurrentScore)  # Initialises the game over screen
                self.game_over_screen_init = True  # Set game over screen initialised to True

            elif self.game_over_screen_init:  # If game over screen initialised is True
                self.GameOverScreen.update(self.CurrentScore, self.Distance_Traveled, self.death_text)  # Calls the GameOverScreen update method

    def Tube_Spawn(self):  # Method to spawn the tube
        tube_gap_position = random.randint(-200, 200)  # Random gap position
        tube_top = TubeLogic(self.ScreenToAddTo, True, tube_gap_position)  # Spawns the top of the tube
        tube_bottom = TubeLogic(self.ScreenToAddTo, False, tube_gap_position)  # Spawns the bottom of the tube
        tube_score_box = TubeScoreLogic(self.ScreenToAddTo)  # Spawns the tube score box
        self.SpriteGroup.add(tube_top, tube_bottom, tube_score_box)  # Adds the sprites to the group
        self.MobGroup.add(tube_top, tube_bottom)  # Adds the sprites to the mob group
        self.TubeHitBoxGroup.add(tube_score_box)  # Adds the sprites to the tube hit box

    def TimerStart(self):  # Method to start a timer which decides the distance between each tube
        self.RandomGap = random.randint(200, 300)  # Random gap time to set the time between the gap
        self.Gap = 0  # Sets the current gap to zero

    def TextUpdate(self):  # Method to update the text on the screen
        if self.GameLive:  # If the game is live
            text_length = len(str(self.CurrentScore))  # Sets the length of the text variable
            score_text = self.text_font.render(str(self.CurrentScore), True,
                                               (0, 0, 0))  # Sets parameters for the button to be used later

            self.ScreenToAddTo.blit(score_text, (10 + (text_length * 9),
                                                 0))  # Superimposes the text on the screen (To show the changing score)

    def game_state_change(self, mouse_position):  # Method to change the game state
        game_state, restart = self.GameOverScreen.game_state_change(mouse_position)  # Sets the game state and restart based on the method
        self.GameLive = True  # Sets game live to true
        self.CurrentScore = 0  # Sets the current score to
        return game_state, restart  # Returns the two variables to the main game loop

    def GameLiveChecker(self):  # Method to check game live
        return self.GameLive  # Returns the game live
