## @file gameObjects.py
#  @brief General classes that are needed for the basic in-game elements
#  @author tasdik, Hongzhao Tan, Nishanth Raveendran, Dananjay Prabaharan

import pygame
#import spaceShooter
from constant import *
from InGameAssets import *
import random

## @brief An abstract data type for storing information of in-game bullet elements
class Bullet(pygame.sprite.Sprite):
    ## @brief The Constructor for class Bullet
    #  @param self The object pointer
    #  @param x The x value of the point where the middile point of the drawn appearance of bullet needs to be initially placed on
    #  @param y The y value of the line where the bottom of the drawn appearance of bullet needs to be initially placed on
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # place the bullet according to the current position of the player
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
	
	## @brief Update the position of the bullet element on the general GUI
    #  @param self The object pointer
    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        # kill the sprite after it moves over the top border
        if self.rect.bottom < 0:
            self.kill()
        # now we need a way to shoot
        # lets bind it to "spacebar".
        # adding an event for it in Game loop

## @brief An abstract data type for storing information of in-game explosion elements
class Explosion(pygame.sprite.Sprite):
	## @brief The Constructor of the class Explosion
    #  @param self The object pointer
    #  @param center The center point of the explosion
    #  @param size The size of the explosion
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75
	
	## @brief Update the appearance of the explosion in the general GUI
    #  @param self The object pointer
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

## @brief An abstract data type for storing the information of in-game missile elements 
class Missile(pygame.sprite.Sprite):
	## @brief The Constructor of the class Missile
    #  @param self The object pointer
    #  @param x The x value of the point where the middile point of the drawn appearance of missile needs to be initially placed on
    #  @param y The y value of the line where the bottom of the drawn appearance of missile needs to be initially placed on
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
	
	## @brief Update the position of the missile element on the general GUI
    #  @param self The object pointer
    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

## @brief An abstract data type for storing the information of in-game meteor elements 
class Mob(pygame.sprite.Sprite):
	## @brief The Constructor of the class Mob
    #  @param self The object pointer
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .90 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        # for randomizing the speed of the Mob
        self.speedy = random.randrange(1, 6)

        # randomize the movements a little more
        self.speedx = random.randrange(-3, 3)

        # adding rotation to the mob element
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8)
        # time when the rotation has to happen
        self.last_update = pygame.time.get_ticks()
	
	## @brief Rotate the appearance of a meteor on the general GUI
    #  @param self The object pointer
    def rotate(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_update > 50:  # in milliseconds
            self.last_update = time_now
            self.rotation = (self.rotation + self.rotation_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
	
	## @brief Update the position of the meteor on the general GUI
    #  @param self The object pointer
    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # now what if the mob element goes out of the screen

        if (self.rect.top > HEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > WIDTH + 20):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            # for randomizing the speed of the Mob
            self.speedy = random.randrange(1, 6)

## @brief An abstract data type for storing the information of in-game alien elements 
class Alien(pygame.sprite.Sprite):
	## @brief The Constructor of the class Alien
    #  @param self The object pointer
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(alien_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .90 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(1, 6)

        # randomize the movements a little more
        self.speedx = random.randrange(-3, 3)

        # time when the rotation has to happen
        self.last_update = pygame.time.get_ticks()
	
	## @brief Update the position of the alien on the general GUI
    #  @param self The object pointer
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # now what if the mob element goes out of the screen

        if (self.rect.top > HEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > WIDTH + 20):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            # for randomizing the speed of the Mob
            self.speedy = random.randrange(1, 6)

## @brief An abstract data type for storing the information of in-game space shooter element 
class Player(pygame.sprite.Sprite):
	## @brief The Constructor of the class Player
    #  @param self The object pointer
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # scale the player img down
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.shield = 100
        self.shoot_delay = DEF_SHOOT_DELAY
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_timer = pygame.time.get_ticks()
	
	## @brief Update the power-up time left, hidden state, and the position on the general GUI of the space shooter
    #  @param self The object pointer
    def update(self):
        # time out for powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power = 1
            self.power_time = pygame.time.get_ticks()

        # unhide
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 30

        self.speedx = 0  # makes the player static in the screen by default.
        self.speedy = 0
        # then we have to check whether there is an event hanlding being done for the arrow keys being
        # pressed

        # will give back a list of the keys which happen to be pressed down at that moment
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 5
        elif keystate[pygame.K_DOWN]:
            self.speedy = 5
        elif keystate[pygame.K_UP]:
            self.speedy = -5
        elif keystate[pygame.K_UP and pygame.K_RIGHT]:
            self.speedy = -5
            self.speedx = 5
        elif keystate[pygame.K_UP and pygame.K_LEFT]:
            self.speedy = -5
            self.speedx = -5
        elif keystate[pygame.K_DOWN and pygame.K_RIGHT]:
            self.speedy = 5
            self.speedx = 5
        elif keystate[pygame.K_DOWN and pygame.K_LEFT]:
            self.speedy = 5
            self.speedx = -5

        # Fire weapons by holding spacebar
        if keystate[pygame.K_SPACE]:
            self.shoot()

        # check for the borders
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

        self.rect.x += self.speedx
        self.rect.y += self.speedy
	
	## @brief Shoots bullets/missile from the space shooter
    #  @param self The object pointer
    def shoot(self):
        # to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                self.shoot_delay = DEF_SHOOT_DELAY
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shooting_sound.play()
            if self.power == 2:
                self.shoot_delay = DEF_SHOOT_DELAY
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shooting_sound.play()
            if self.power == 3:
                # Missile shoots from center of ship
                self.shoot_delay = DEF_SHOOT_DELAY
                missile1 = Missile(self.rect.centerx, self.rect.top)
                all_sprites.add(missile1)
                missles.add(missile1)
                shooting_sound.play()
                missile_sound.play()
            if self.power == 4:
                self.shoot_delay = DEF_SHOOT_DELAY // 2
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shooting_sound.play()
	
	## @brief Adjust the value of power the space shooter currently has
    #  @param self The object pointer
    #  @param p The new value of power that is assigned to the space shooter
    def powerup(self, p):
        self.power = p
        self.power_time = pygame.time.get_ticks()
	
	## @brief Turns the space shooter to be hidden to avoid being hit by any mob
    #  @param self The object pointer
    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

## @brief An abstract data type for storing the information of in-game power-up buff elements
class Pow(pygame.sprite.Sprite):
	## @brief The Constructor of the class Pow
    #  @param self The object pointer
    #  @param center The center point where the power-up buff is generated on the general GUI
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun', 'missl', 'rapid'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # place the bullet according to the current position of the player
        self.rect.center = center
        self.speedy = 2
	
	## @brief Update the position of the power-up buff on the general GUI
    #  @param self The object pointer
    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        # kill the sprite after it moves over the top border
        if self.rect.top > HEIGHT:
            self.kill()
