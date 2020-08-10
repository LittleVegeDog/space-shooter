## @file __init__.py
#  @brief Mark directories needed on disk as Python package directories
#  @author tasdik, Hongzhao Tan, Nishanth Raveendran, Dananjay Prabaharan

import pygame
from constant import WIDTH,HEIGHT

pygame.init()
pygame.mixer.init()  ## For sound

## @var screen The window that conatins the general GUI
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

## @var clock The clock that records the general in-game time
clock = pygame.time.Clock()     ## For syncing the FPS