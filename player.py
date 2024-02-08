import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position, blocks_player, group):
        super().__init__(group)
        self.image = pygame.Surface((25,25))
        self.rect = self.image.get_rect(topleft = position)
        self.image.fill('blue')
        self.player_move = pygame.math.Vector2()
        self.speed = 7
        self.spell_group = pygame.sprite.Group()
        self.blocks_player = blocks_player

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            self.player_move.y = 1
        elif keys[pygame.K_w]:
            self.player_move.y = -1
        else:
            self.player_move.y = 0

        if keys[pygame.K_d]:
            self.player_move.x = 1
        elif keys[pygame.K_a]:
            self.player_move.x = -1
        else:
            self.player_move.x = 0

    def moving(self):
        self.rect.centerx += self.player_move.x * self.speed
        self.check_collisions(self.blocks_player, 'x')
        self.rect.centery += self.player_move.y * self.speed
        self.check_collisions(self.blocks_player, 'y')

    def check_collisions(self, blocks , dir):
        if dir == 'x':
            coll = pygame.sprite.spritecollide(self ,blocks,False)
            if coll:
                if self.player_move.x > 0:
                    self.rect.x = coll[0].rect.left - self.rect.width
                if self.player_move.x < 0:
                    self.rect.x = coll[0].rect.right

        if dir == 'y':
            coll = pygame.sprite.spritecollide(self ,blocks,False)
            if coll:
                if self.player_move.y > 0:
                    self.rect.y = coll[0].rect.top - self.rect.height
                if self.player_move.y < 0:
                    self.rect.y = coll[0].rect.bottom
    
    def update(self):
        self.player_input()
        self.moving()
        