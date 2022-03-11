# Importing the required libraries for the code to work
import pygame
from bullet import BulletClass


# Code for the class of the bird sprite
class BirdClass(pygame.sprite.Sprite):
    def __init__(self, screen, all_sprite_group, bullet_group):  # Method called when class is instantiated
        pygame.sprite.Sprite.__init__(self)  # Inherits the parent Sprite class
        self.ScreenToAddTo = screen  # Gets the screen that is needed to be added to
        self.Jump_Height = 15  # Sets the jump height of the bird
        self.ScreenPosX = 150  # Sets the stating X position
        self.ScreenPosY = 0  # Sets the starting Y position
        self.Gravity = -1  # Sets the gravity that the bird abides

        self.BulletGroup = bullet_group

        self.SpriteGroup = all_sprite_group
        self.SpriteBullets = pygame.sprite.Group()  # Creates a tub_hit_box group

        self.Sprites = []  # Creates a list of sprites for animation
        self.Current_Animation_State = 0  # Sets the current animation state
        self.AnimationTimer = 10  # Animation timer set gap between the images

        self.fly_sound = pygame.mixer.Sound("Sounds/SoundEffects/fly.mp3")  # Sets the fly sound

        for i in range(4):  # Runs four times the amount of bird images
            filename = 'Sprites/BirdSprite/StandardBird/frame-{}.png'.format(i)  # Sets the current sprite file
            img = pygame.image.load(filename).convert()  # Converts the filename
            img.set_colorkey((18, 255, 0))  # Removes the background
            img_scale = pygame.transform.scale(img, (75, 75))  # Scales the large explosion
            self.Sprites.append(img_scale)  # Apply transformation

        self.FlyCoolDown = 60  # Sets the time needed between presses of the fly button
        self.Acceleration = 0  # Sets the starting acceleration

        self.rect = self.Sprites[0].get_rect()  # Defines the rectangular hit box of a sprite
        self.radius = int(self.rect.width * 1.40)  # Defines the circle hit box for the sprite
        self.rect.x = self.ScreenPosX  # Sets the x position of the hit box
        self.rect.y = self.ScreenPosY  # Sets the y position of the hit box
        # pygame.draw.circle(self.Sprite, (255, 0, 0), self.rect.center, self.radius)

    def update(self, game_live):  # Method called to update the bird sprite
        self.AnimationTimer -= 1  # Animation timer is reduced by 1

        if self.Acceleration < 10:  # If Acceleration is less than 10
            self.Acceleration += 1  # Acceleration incremented by 1

        self.ScreenPosY += self.Acceleration  # Calculates the effect the acceleration has
        self.rect.y += self.Acceleration  # Moves the hit box with the sprite

        self.SpriteBullets.update(game_live)

        angle = self.Acceleration * -3  # Calculates the angle for sprite based on acceleration
        rotated_sprite = pygame.transform.rotate(self.Sprites[self.Current_Animation_State], angle)  # Sets the amount to rotate the sprite

        self.ScreenToAddTo.blit(rotated_sprite, (self.ScreenPosX, self.ScreenPosY))  # Blitz the changes to the screen

        if self.Current_Animation_State != 0 and self.AnimationTimer < 0:  # If the animation state does not equal zero and timer run down
            self.Current_Animation_State -= 1  # Decreases the current animation state by 1

        if not game_live:  # If game is not live
            self.kill()  # Kills the sprite

    def AutoFly(self):  # Auto fly method to be used within the menu
        if self.ScreenPosY >= 360:  # If the spite fulls below a certain threshold in the Y axis
            self.Acceleration = -20  # Sprite counteracts the full by using acceleration
            self.Current_Animation_State = 3  # Sets the animation state
            self.AnimationTimer = 5  # Sets the animation timer
            pygame.mixer.Sound.play(self.fly_sound)  # Plays the fly sound

    def ShopScreen(self):  # Method used within the shop screen menu
        self.ScreenToAddTo.blit(self.Sprites[self.Current_Animation_State], (635, 325))  # Sets the position used in the menu
        self.Current_Animation_State = 0

    def Fly(self):  # Method that is assigned to a key press which accelerates the sprite up
        self.Acceleration = - self.Jump_Height  # Sprite counteracts the full by using acceleration
        self.Current_Animation_State = 3  # Sets the animation state
        self.AnimationTimer = 5  # sets the animation timer
        pygame.mixer.Sound.play(self.fly_sound)  # Plays the fly sound

    def KillSprite(self):
        self.kill()

    def Shoot(self):
        bullet_class = BulletClass(self.ScreenToAddTo, self.ScreenPosX, self.rect.y, True)  # Spawns the tube score box
        self.SpriteGroup.add(bullet_class)  # Adds the sprites to the group
        self.BulletGroup.add(bullet_class)  # Adds the sprites to the group
        