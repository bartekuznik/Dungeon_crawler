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

game_start = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MANA_REGEN_EVENT and game_start:
            level_base.player.mana_regeneration()
        if event.type == pygame.KEYDOWN and (game_start == 2 or game_start == 4):
            if event.key == pygame.K_SPACE:
                game_start = 3

    if game_start == 1:
        screen.fill('black')
        restart = level_base.update()
        if restart == -1:
            game_start = 2
        elif restart == -2:
            game_start = 4

    elif game_start == 2:
        screen.fill('black')
        top_text = text_font.render('Wygrales!!!!',False,'blue')
        bottom_text = text_font.render('Kliknij SPACJE',False,'red')
        top_text_rect = top_text.get_rect(center = (400, 230))
        bottom_text_rect = top_text.get_rect(center = (320, 250))
        screen.blit(top_text, top_text_rect)
        screen.blit(bottom_text, bottom_text_rect)

    elif game_start == 4:
        screen.fill('black')
        top_text = text_font.render('Zginales',False,'red')
        bottom_text = text_font.render('Kliknij SPACJE',False,'red')
        top_text_rect = top_text.get_rect(center = (400, 180))
        bottom_text_rect = top_text.get_rect(center = (320, 250))
        screen.blit(top_text, top_text_rect)
        screen.blit(bottom_text, bottom_text_rect)

    elif game_start == 3:
        gui = GUI(screen, text_font)
        important_table = gui.run()
        level_base = LevelBase(screen, level_date_tabel, important_table)
        #print(important_table)
        game_start = 1

    pygame.display.update()
    clock.tick(60)