import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, image_value, position,group):
        super().__init__(group)
        self.image = pygame.image.load(image_value).convert()
        self.rect = self.image.get_rect(topleft = position)
        #self.image.fill('red')
        