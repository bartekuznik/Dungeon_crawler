import pygame

class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((30,60))
        self.rect = self.image.get_rect(topleft = position)
        self.image.fill('green')

    def movement(self):
        pass

    def update(self, enemies):
        for enemy in enemies:
            enemy.movement()