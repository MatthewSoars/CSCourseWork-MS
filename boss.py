import pygame
import random
from WallSpawner import WallLogic


# Code for the class of the bird sprite
class BossClass(pygame.sprite.Sprite):
    def __init__(self, screen, all_sprite_group, wall_group):
        pygame.sprite.Sprite.__init__(self)  # Inherits the parent Sprite class
        self.ScreenToAddTo = screen  # Gets the screen that is needed to be added to
        self.ScreenPosX = 1200  # Sets the stating X position
        self.ScreenPosY = 70  # Sets the starting Y position

        self.WallGroup = wall_group

        self.SpriteGroup = all_sprite_group
        self.SpriteBullets = pygame.sprite.Group()  # Creates a tub_hit_box group

        self.Sprites = []  # Creates a list of sprites for animation
        self.Current_Animation_State = 0  # Sets the current animation state
        self.AnimationTimer = 10  # Animation timer set gap between the images

        self.fly_sound = pygame.mixer.Sound("Sounds/SoundEffects/fly.mp3")  # Sets the fly sound

        for i in range(4):  # Runs four times the amount of bird images
            filename = 'Sprites/BossSprite/frame-{}.png'.format(i)  # Sets the current sprite file
            img = pygame.image.load(filename).convert()  # Converts the filename
            img.set_colorkey((17, 0, 255))  # Removes the background
            img_scale = pygame.transform.scale(img, (100, 120))  # Scales the large explosion
            self.Sprites.append(img_scale)  # Apply transformation

        self.rect = self.Sprites[0].get_rect()  # Defines the rectangular hit box of a sprite
        self.radius = int(self.rect.width * 1.40)  # Defines the circle hit box for the sprite
        self.rect.x = self.ScreenPosX  # Sets the x position of the hit box
        self.rect.y = self.ScreenPosY  # Sets the y position of the hit box
        # pygame.draw.circle(self.Sprite, (255, 0, 0), self.rect.center, self.radius)
        self.Speed = 3
        self.Downwards = True
        
        self.WallSpawnerTimer = 20

    def update(self, game_live):  # Method called to update the bird sprite
        if game_live:
            self.AnimationTimer -= 1  # Animation timer is reduced by 1
            self.WallSpawnerTimer -= 1

            if self.ScreenPosY > 600 and self.Downwards:
                self.Downwards = False

            if self.ScreenPosY < 50 and not self.Downwards:
                self.Downwards = True

            if self.Downwards:
                self.ScreenPosY += self.Speed

            if not self.Downwards:
                self.ScreenPosY -= self.Speed

            if self.Current_Animation_State == 0:
                self.Current_Animation_State = 3
                self.AnimationTimer = 7

            if self.Current_Animation_State != 0 and self.AnimationTimer < 0:  # If the animation state does not equal zero and timer run down
                self.Current_Animation_State -= 1  # Decreases the current animation state by 1

            if self.WallSpawnerTimer <= 0:
                BossClass.Shoot(self)

            self.ScreenToAddTo.blit(self.Sprites[self.Current_Animation_State],
                                    (self.ScreenPosX, self.ScreenPosY))  # Blitz the changes to the screen

    def Shoot(self):
        wall_class = WallLogic(self.ScreenToAddTo, self.ScreenPosX, self.ScreenPosY)  # Spawns the tube score box
        self.SpriteGroup.add(wall_class)  # Adds the sprites to the sprite group
        self.WallGroup.add(wall_class)  # Adds the sprites to the bullet group
        self.WallSpawnerTimer = random.randint(20, 80)
