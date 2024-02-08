import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, size, position,group):
        super().__init__(group)
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft = position)
        self.image.fill('red')
        