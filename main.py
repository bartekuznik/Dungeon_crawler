import pygame
import sys
from level import *
from level_tables import *

pygame.init()

screen_w, screen_h = 700, 500
screen = pygame.display.set_mode((screen_w,screen_h))
clock = pygame.time.Clock()

level_base = LevelBase(screen, level_date_tabel)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill('black')
    level_base.update()

    pygame.display.update()
    clock.tick(60)