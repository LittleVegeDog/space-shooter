## @file constant.py
#  @brief Constants that need to extract data from files in the assets folders
#  @author tasdik, Hongzhao Tan, Nishanth Raveendran, Dananjay Prabaharan

from os import path
import pygame
from constant import BLACK
# Assets Folder
## @var img_dir Path to the directory of images that are needed
img_dir = path.join(path.dirname(__file__), 'assets')
## @var img_dir Path to the directory of sounds that are needed
sound_folder = path.join(path.dirname(__file__), 'sounds')

# Explosion Animation
## @var explosion_anim Dictionary that consists of the data needed for the in-game explosion animation
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    # resize the explosion
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)

    # player explosion
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)


# All in-game sprites
## @var all_sprites All in-game elements that are shown on the general GUI 
all_sprites = pygame.sprite.Group()
## @var bullets All elements which represent the bullets that are shown on the general GUI
bullets = pygame.sprite.Group()
## @var missiles All elements which represent the missiles that are shown on the general GUI
missles = pygame.sprite.Group()
## @var powerups All elements which represent the power-up buffs for the space shooter that are shown on the general GUI
powerups = pygame.sprite.Group()
## @var mobs All elements which represent the meteors that are shown on the general GUI
mobs = pygame.sprite.Group()
## @var aliens All elements which represent the aliens that are shown on the general GUI
aliens = pygame.sprite.Group()


# Sounds
## @var shooting_sound Sound of the space shooter shooting bullets
shooting_sound = pygame.mixer.Sound(path.join(sound_folder, 'pew.wav'))
## @var missile_sound Sound of the space shooter shooting missiles
missile_sound = pygame.mixer.Sound(path.join(sound_folder, 'rocket.ogg'))
## @var expl_sound Sound of the explosion of mobs
expl_sounds = []
for sound in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_folder, sound)))
## @var player_death_sound Sound of the death of the space shooter
player_die_sound = pygame.mixer.Sound(path.join(sound_folder, 'rumble1.ogg'))

# In-game object images
## @var player_img Image used for the appearance of the space shooter
player_img = pygame.image.load(path.join(img_dir, 'playerShip1_orange.png')).convert()
## @var player_mini_img Image used for the appearance of the space shooter that is properly sized to suit the size of the general GUI
player_mini_img = pygame.transform.scale(player_img, (25, 19))

## @var bullet_img Image used for the appearance of the bullets
bullet_img = pygame.image.load(path.join(img_dir, 'laserRed16.png')).convert()
## @var missile_img Image used for the appearance of the missiles
missile_img = pygame.image.load(path.join(img_dir, 'missile.png')).convert_alpha()

## @var meteor_images List that contains all images that are used for the appearances of the meteors of different sizes
meteor_images = []
meteor_list = [
    'meteorBrown_big1.png',
    'meteorBrown_big2.png',
    'meteorBrown_med1.png',
    'meteorBrown_med3.png',
    'meteorBrown_small1.png',
    'meteorBrown_small2.png',
    'meteorBrown_tiny1.png'
]
for image in meteor_list:
    meteor_images.append(pygame.image.load(
        path.join(img_dir, image)).convert())

## @var alien_images List that contains all images that are used for the appearance of differnent types of aliens
alien_images = []
alien_list = ['alienShip.png']
for image in alien_list:
    alien_images.append(pygame.image.load(path.join(img_dir, image)).convert())

## @var powerup_images List that contains all images that are used for the appearance of differnent types of power-up buffs
powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'x2.png')).convert()
powerup_images['missl'] = pygame.image.load(path.join(img_dir, 'm.png')).convert()
powerup_images['rapid'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()

# Font for text
## @var font_name The font that is used for all of the text displayed on the general GUI
font_name = pygame.font.match_font('arial')

# Background
## @var background The image that is used for the appearance of the background of the general GUI
background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
## @var background_rect The dimensions of the appearance of the background 
background_rect = background.get_rect()
