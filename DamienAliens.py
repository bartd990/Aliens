import random
import os.path
import pygame
from pygame.locals import Rect, QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_SPACE, \
    K_ESCAPE, FULLSCREEN
from Alien import Alien
from Bomb import Bomb
from Explosion import Explosion
from Player import Player
from PlayerLives import PlayerLives
from Score import Score
from Shot import Shot
import Utility
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")
MAX_SHOTS = 2
ALIEN_ODDS = 22
BOMB_ODDS = 60
ALIEN_RELOAD = 12
SCREENRECT = Rect(0, 0, 1024, 768)
main_directory = os.path.split(os.path.abspath(__file__))[0]
