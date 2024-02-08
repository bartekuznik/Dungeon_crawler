import pygame
from level_tables import *
from player import *
from block import * 
from end_level import *

w = 2000
h = 2000
block_size = 50

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
                if cell == "a":
                    block = Block( block_size, (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == "e":
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
        self.sprite_group.custom_draw(self.player)
        self.sprite_group.update()

        #self.player.update() -> self.sprite_group.update() już to wykonuje
        self.collide_end()

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

	def custom_draw(self,player):
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)