import pygame
import math

class Spell(pygame.sprite.Sprite):
    def __init__(self, position, group, blocks):
        super().__init__(group)
        self.image = pygame.Surface((5,5))
        self.rect = self.image.get_rect(center = position)
        self.image.fill('brown')
        self.blocks = blocks
        self.speed = 10
        self.target_position = pygame.mouse.get_pos()

    def moving(self):
        mouse_pos = pygame.mouse.get_pos()
        
        # Oblicz wektor od pocisku do myszy
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery
        
        # Oblicz długość wektora
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        # Sprawdź, czy długość wektora jest większa niż 0, aby uniknąć dzielenia przez zero
        if distance != 0:
            # Znormalizuj wektor kierunku
            direction_x = dx / distance
            direction_y = dy / distance
            
            # Przesuń pocisk wzdłuż wektora kierunku
            self.rect.x += direction_x * self.speed
            self.rect.y += direction_y * self.speed

    def bullet_wall_collisions(self): 
        coll = pygame.sprite.spritecollide(self, self.blocks, False)
        if coll:
           self.kill()
                
    
    def update(self):
        self.moving()
        self.bullet_wall_collisions()