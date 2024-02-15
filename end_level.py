import pygame

class EndLevel(pygame.sprite.Sprite):
    def __init__(self, size, position, group):
        super().__init__(group)
        self.image = pygame.image.load('images/tile030.png').convert()
        self.rect = self.image.get_rect(topleft = position)
        #self.image.fill('yellow')