from typing import Any
import pygame
from block import *
from config import *

class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, position, group, player, block_group):
        super().__init__(group)
        #self.image = pygame.Surface((16,16))
        #self.rect = self.image.get_rect(topleft = position)
        #self.image.fill('green')
        self.player = player
        self.image = pygame.image.load('images/enemy/monster.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.enemy_pos = pygame.Vector2(self.rect.center)
        self.enemy_saw_player = False

        self.direction = pygame.Vector2()
        self.block_group = block_group
        self.speed = 1

        self.attack_damage = 200
        self.health = 200


    def movement(self):
        distance = ((self.player.rect.centerx - self.rect.centerx)**2 + (self.player.rect.centery - self.rect.centery)**2)**(1/2)
        if distance < 300 or self.enemy_saw_player == True:
            self.enemy_saw_player = True
            player_pos = pygame.Vector2(self.player.rect.center)
            enemy_pos = pygame.Vector2(self.rect.center)

            self.direction = (player_pos - enemy_pos).normalize()

            self.rect.x += self.direction.x * self.speed
            self.check_collisions(self.block_group, 'x')
            self.rect.y += self.direction.y * self.speed
            self.check_collisions(self.block_group, 'y')
    
    def check_collisions(self, blocks , dir):
        if dir == 'x':
            coll = pygame.sprite.spritecollide(self ,blocks,False)
            if coll:
                if self.direction.x > 0:
                    self.rect.x = coll[0].rect.left - self.rect.width
                if self.direction.x < 0:
                    self.rect.x = coll[0].rect.right

        if dir == 'y':
            coll = pygame.sprite.spritecollide(self ,blocks,False)
            if coll:
                if self.direction.y > 0:
                    self.rect.y = coll[0].rect.top - self.rect.height
                if self.direction.y < 0:
                    self.rect.y = coll[0].rect.bottom

    def death(self):
        if self.health <= 0:
            self.kill()

    def update(self):
        self.movement()
        self.death()


class TowerEnemy(pygame.sprite.Sprite):
    def __init__(self, position, group, player, blocks, e_spell_group):
        super().__init__(group)
        self.group = group
        #self.image = pygame.Surface((16,16))
        #self.rect = self.image.get_rect(topleft = position)
        #self.image.fill('green')
        self.image = pygame.image.load('images/enemy/wizzard.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (34,30))
        self.rect = self.image.get_rect(topleft = position)
        self.enemy_pos = pygame.Vector2(self.rect.center)
        self.attack_damage = 500
        self.player = player
        self.blocks = blocks
        self.e_spell_group = e_spell_group
        self.attack_cooldown = 3000  # Czas między atakami w milisekundach
        self.last_attack_time = pygame.time.get_ticks()
        self.health = 100


    def get_spell_direction(self):
        player_pos = pygame.Vector2(self.player.rect.center)    
        self.spell_direction = (player_pos - self.enemy_pos).normalize()

    def cast_spell(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time > self.attack_cooldown:
            spell = Spell(self.rect.center, self.spell_direction, self.group, self.blocks)
            self.e_spell_group.add(spell)
            self.last_attack_time = current_time

    def death(self):
        if self.health <= 0:
            self.kill()

    def update(self):
        self.get_spell_direction()
        self.cast_spell()
        self.death()

class Boss(pygame.sprite.Sprite):
    def __init__(self, position, group, player, blocks, e_spell_group):
        super().__init__(group)
        #self.image = pygame.Surface((16,16))
        #self.rect = self.image.get_rect(topleft = position)
        #self.image.fill('blue')
        self.player = player
        self.image = pygame.image.load('images/enemy/imp.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.enemy_pos = pygame.Vector2(self.rect.center)
        self.enemy_saw_player = False
        self.health = 900
        self.direction = pygame.Vector2()
        self.blocks = blocks
        self.speed = 1
        self.group = group
        self.e_spell_group = e_spell_group

        self.attack_cooldown = 3000  # Czas między atakami w milisekundach
        self.last_attack_time = pygame.time.get_ticks()

        self.attack_damage = 1000

    def movement(self):
        distance = ((self.player.rect.centerx - self.rect.centerx)**2 + (self.player.rect.centery - self.rect.centery)**2)**(1/2)
        if distance < 300 or self.enemy_saw_player == True:
            self.enemy_saw_player = True
            player_pos = pygame.Vector2(self.player.rect.center)
            enemy_pos = pygame.Vector2(self.rect.center)

            self.direction = (player_pos - enemy_pos).normalize()

            self.rect.x += self.direction.x * self.speed
            self.check_collisions(self.blocks, 'x')
            self.rect.y += self.direction.y * self.speed
            self.check_collisions(self.blocks, 'y')
    
    def check_collisions(self, blocks , dir):
        if dir == 'x':
            coll = pygame.sprite.spritecollide(self ,blocks,False)
            if coll:
                if self.direction.x > 0:
                    self.rect.x = coll[0].rect.left - self.rect.width
                if self.direction.x < 0:
                    self.rect.x = coll[0].rect.right

        if dir == 'y':
            coll = pygame.sprite.spritecollide(self ,blocks,False)
            if coll:
                if self.direction.y > 0:
                    self.rect.y = coll[0].rect.top - self.rect.height
                if self.direction.y < 0:
                    self.rect.y = coll[0].rect.bottom

    def cast_spell(self, spell_tab):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time > self.attack_cooldown:
            for index in range(len(spell_tab)):
                spell = Spell(self.rect.center, pygame.Vector2(spell_tab[index][0], spell_tab[index][1]), self.group, self.blocks)
                self.e_spell_group.add(spell)
            self.last_attack_time = current_time
    
    def death(self):
        if self.health <= 0:
            self.kill()

    def update(self):
        self.movement()
        self.death()

        if self.health > 600:
            self.cast_spell([[1,0], [-1,0],[0,1],[0,-1]])
        elif self.health > 300 and self.health <= 600:
            self.cast_spell([[-0.75 , 0.75], [0.75 , -0.75],[-0.75, -0.75],[0.75 , 0.75]])
        elif self.health <= 300:
            self.cast_spell([[-0.75 , 0.75], [0.75 , -0.75],[-0.75, -0.75],[0.75 , 0.75], [1,0], [-1,0],[0,1],[0,-1]])