import pygame
import sys
from level import *
from config import *
from gui import *

pygame.init()

screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/Silkscreen-Regular.ttf', 40)
#text_font  = pygame.font.SysFont('arial', 40)
pygame.display.set_caption('Dungeon Crawler')
MANA_REGEN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MANA_REGEN_EVENT, 1000) 

game_start = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MANA_REGEN_EVENT and game_start:
            level_base.player.mana_regeneration()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                level_base.player.damage(100)

    if game_start:
        screen.fill('black')
        restart = level_base.update()
        if restart == -1:
            game_start = False
    else:
        gui = GUI(screen, text_font)
        important_table = gui.run()
        level_base = LevelBase(screen, level_date_tabel, important_table)
        #print(important_table)
        game_start = True

    pygame.display.update()
    clock.tick(60)