import pygame
import pygame.math
import math

class Block(pygame.sprite.Sprite):
    def __init__(self, image_value, position,group):
        super().__init__(group)
        self.image = pygame.image.load(image_value).convert()
        self.rect = self.image.get_rect(topleft = position)
        

class EndLevel(pygame.sprite.Sprite):
    def __init__(self, size, position, group):
        super().__init__(group)
        self.image = pygame.image.load('images/tiles/tile030.png').convert()
        self.rect = self.image.get_rect(topleft = position)

class Key(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('images/tiles/tile092.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)


class Spell(pygame.sprite.Sprite):
    def __init__(self, position,  direction, group, blocks):
        super().__init__(group)
        self.image = pygame.image.load('images/spell/FB001.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image,(0.5))
        self.blocks = blocks
        self.speed = 8
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000
        self.direction = direction
        angle = math.degrees(math.atan2(-self.direction.y, self.direction.x))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=position)

    def spell_wall_collisions(self):
        coll = pygame.sprite.spritecollide(self, self.blocks, False)
        if coll:
            self.kill()

    def move(self):
        self.rect.center += self.direction *self.speed
        
    def update(self):
        self.move()
        self.spell_wall_collisions()

class Potion(pygame.sprite.Sprite):
    def __init__(self, position, image_value, value, type, group):
        super().__init__(group) 
        self.image = pygame.image.load(image_value).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.value = value
        self.type = type