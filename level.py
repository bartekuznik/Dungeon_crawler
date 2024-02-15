import pygame
from level_tables import *
from player import *
from block import * 
from end_level import *

w = 2000
h = 2000
block_size = 32

class LevelBase():
    def __init__(self, screen, level_date_table):
        self.screen = screen
        self.level_number = 0
        self.level_date = level_date_table[self.level_number]
        self.block_group = pygame.sprite.Group()
        self.sprite_group = YSortCameraGroup()
        self.setup_level(self.level_date)
        
    def setup_level(self, level_date):
        self.player_group = pygame.sprite.GroupSingle()
        self.end_group = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(level_date):
            for cell_index, cell in enumerate(row):
                x = cell_index * block_size
                y = row_index * block_size
                if cell == 2:
                    block = Block( 'images/tile002.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 3:
                    block = Block( 'images/tile003.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 4:
                    block = Block( 'images/tile004.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)  
                if cell == 5:
                    block = Block( 'images/tile005.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 8:
                    block = Block( 'images/tile008.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 12:
                    block = Block( 'images/tile012.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 13:
                    block = Block( 'images/tile013.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 14:
                    block = Block( 'images/tile014.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 22:
                    block = Block( 'images/tile022.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 23:
                    block = Block( 'images/tile023.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 24:
                    block = Block( 'images/tile024.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)  
                if cell == 30:
                    block = Block( 'images/tile030.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 32:
                    block = Block( 'images/tile032.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 33:
                    block = Block( 'images/tile033.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 34:
                    block = Block( 'images/tile034.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 35:
                    block = Block( 'images/tile035.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 38:
                    block = Block( 'images/tile038.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)  
                if cell == 45:
                    block = Block( 'images/tile045.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)  
                if cell == 55:
                    block = Block( 'images/tile055.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 65:
                    block = Block( 'images/tile065.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 66:
                    block = Block( 'images/tile066.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 30:
                    self.end_level = EndLevel(block_size, (x,y),[self.sprite_group])
                    self.end_group.add(self.end_level)
                if cell == "p":
                    self.player = Player((x,y), self.block_group,[self.sprite_group])
                    self.player_group.add(self.player)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.block_group)
        self.all_sprites.add(self.end_group)

        
    def collide_end(self):
        if self.player.rect.colliderect(self.end_level):
            self.level_number += 1
            self.all_sprites.empty()
            self.block_group.empty()
            self.player_group.empty()
            self.end_group.empty()
            self.sprite_group.empty()
            self.next_level()


    def next_level(self):
        self.level_date = level_date_tabel[self.level_number]
        self.setup_level(self.level_date)


    def update(self):
        
        #self.block_group.draw(self.screen)
        #self.player_group.draw(self.screen)
        #self.end_group.draw(self.screen)
        
        self.sprite_group.update()
        self.sprite_group.custom_draw(self.player)
        #self.player.update() -> self.sprite_group.update() już to wykonuje
        self.collide_end()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.back = pygame.image.load('images/level_1.png').convert()
        self.back_rect = self.back.get_rect(topleft = (0,0))
        
    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        back_offset = self.back_rect.topleft - self.offset
        self.display_surface.blit(self.back,back_offset)

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)