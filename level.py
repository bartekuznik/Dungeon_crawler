import pygame
from config import *
from player import *
from block import * 
from enemy import *
import numpy as np



class LevelBase():
    def __init__(self, screen, level_date_table, important_table):
        self.screen = screen
        self.level_number = 0
        self.level_date = level_date_table[self.level_number]
        self.number_of_level = len(level_date_tabel)
        self.block_group = pygame.sprite.Group()
        self.sprite_group = Allsprites(self.level_number)
        self.enemy_group = pygame.sprite.Group()
        self.spell_group = pygame.sprite.Group()
        self.enemy_spell_group = pygame.sprite.Group()
        self.potion_group = pygame.sprite.Group()
        self.key_group = pygame.sprite.GroupSingle()

        self.player_direction = pygame.Vector2(1,0)

        self.can_shoot = True
        self.sword = None
        self.attack_cooldown = 500  # Czas między atakami w milisekundach
        self.last_attack_time = pygame.time.get_ticks()

        self.game_state = 'exploration'
        self.end_game = False
        self.important_table = important_table

        self.is_calm = True

        self.have_key = False

        self.is_fading = False
        self.fade_start_time = None
        self.fade_duration = 500

        self.next_time = pygame.time.get_ticks() + 650

        self.setup_level(self.level_date)
        
    def setup_level(self, level_date):

        if self.important_table[0] == True:
            self.linear_music()
        elif self.important_table[1] == True:
            self.adaptive_music()
        elif self.important_table[2] == True:
            self.generative_music()

        self.player_group = pygame.sprite.GroupSingle()
        self.end_group = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(level_date):
            for cell_index, cell in enumerate(row):
                x = cell_index * BLOCK_SIZE
                y = row_index * BLOCK_SIZE
                
                #walls blocks

                if cell == 2:
                    block = Block( 'images/tiles/tile002.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 3:
                    block = Block( 'images/tiles/tile003.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 4:
                    block = Block( 'images/tiles/tile004.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)  
                if cell == 5:
                    block = Block( 'images/tiles/tile005.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 8:
                    block = Block( 'images/tiles/tile008.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 12:
                    block = Block( 'images/tiles/tile012.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 13:
                    block = Block( 'images/tiles/tile013.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 14:
                    block = Block( 'images/tiles/tile014.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 22:
                    block = Block( 'images/tiles/tile022.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 23:
                    block = Block( 'images/tiles/tile023.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 24:
                    block = Block( 'images/tiles/tile024.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)  
                if cell == 32:
                    block = Block( 'images/tiles/tile032.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 33:
                    block = Block( 'images/tiles/tile033.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 34:
                    block = Block( 'images/tiles/tile034.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 35:
                    block = Block( 'images/tiles/tile035.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 38:
                    block = Block( 'images/tiles/tile038.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)  
                if cell == 45:
                    block = Block( 'images/tiles/tile045.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)  
                if cell == 55:
                    block = Block( 'images/tiles/tile055.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 65:
                    block = Block( 'images/tiles/tile065.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)
                if cell == 66:
                    block = Block( 'images/tiles/tile066.png', (x,y),[self.sprite_group])
                    self.block_group.add(block)

                #end_level

                if cell == 30:
                    self.end_level = EndLevel(BLOCK_SIZE, (x,y),[self.sprite_group])
                    self.end_group.add(self.end_level)

                #key
                if cell == "k":
                    self.key = Key((x,y),[self.sprite_group])
                    self.key_group.add(self.key)

                #potions

                if cell == "bh":
                    potion = Potion((x,y), 'images/potions/big_health.png', 400, 'health',[self.sprite_group])
                    self.potion_group.add(potion)
                if cell == "sh":
                    potion = Potion((x,y), 'images/potions/small_health.png', 100, 'health',[self.sprite_group])
                    self.potion_group.add(potion)
                if cell == "bm":
                    potion = Potion((x,y), 'images/potions/big_mana.png', 400, 'mana',[self.sprite_group])
                    self.potion_group.add(potion)
                if cell == "sm":
                    potion = Potion((x,y), 'images/potions/small_mana.png', 100, 'mana',[self.sprite_group])
                    self.potion_group.add(potion)

                #player

                if cell == "p":
                    self.player = Player((x,y), self.block_group,[self.sprite_group], self.screen, self.sword_attack, self.hide_sword)
                    self.player_group.add(self.player)

                #enemies

                if cell == "e":
                    enemy = BaseEnemy((x,y),[self.sprite_group], self.player, self.block_group)
                    self.enemy_group.add(enemy)
                if cell == "t":
                    enemy = TowerEnemy((x,y), [self.sprite_group] ,self.player, self.block_group, self.enemy_spell_group)
                    self.enemy_group.add(enemy)
                if cell == "b":
                    enemy = Boss((x,y),[self.sprite_group], self.player, self.block_group, self.enemy_spell_group)
                    self.enemy_group.add(enemy)


        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.block_group)
        self.all_sprites.add(self.potion_group)
        self.all_sprites.add(self.end_group)

    def linear_music(self):
        self.music = pygame.mixer.Sound('linear/super_mario.mp3')
        self.music.set_volume(0.8)
        self.music.play(loops=-1)

    def adaptive_music(self):
        sound_paths = {
            "exploration": "adaptive/Exploration.mp3",
            "close_to_enemy": "adaptive/Enemy.mp3",
            "battle": "adaptive/Battle.mp3"
        }
        
        self.sounds = {state: pygame.mixer.Sound(path) for state, path in sound_paths.items()}
        self.current_state = self.game_state
        self.music = self.sounds[self.game_state]
        self.music.play(loops=-1)
        self.music.set_volume(0.8)

    def generative_music(self):
        self.calm_chords_mp3 = {
            'C Major': 'test_2/C Major.mp3',
            'Dm7': 'test_2/Dm7.mp3',
            'G7': 'test_2/G7.mp3',
            'Cmaj7': 'test_2/Cmaj7.mp3',
            'Am': 'test_2/Am.mp3',
            'Dm': 'test_2/Dm.mp3',
            'G Major': 'test_2/G Major.mp3',
            'F Major': 'test_2/F Major.mp3'
        }

        self.high_tension_chords_mp3 = {
            'G Major': 'test_2/G Major.mp3',
            'C Major': 'test_2/C Major.mp3',
            'Am': 'test_2/Am.mp3',
            'F Major': 'test_2/F Major.mp3',
            'E Major': 'test_2/E Major.mp3',
            'Dm7': 'test_2/Dm7.mp3',
            'G7': 'test_2/G7.mp3',
            'Cmaj7': 'test_2/Cmaj7.mp3',
            'A7': 'test_2/A7.mp3'
        }

        self.calm_transition_matrix = np.array([
            [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0],  # C Major
            [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Dm7
            [0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0],  # G7
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Cmaj7
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],  # Am
            [0.0, 0.0, 0.5, 0.0, 0.5, 0.0, 0.0, 0.0],  # Dm
            [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],  # G Major
            [0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.0],  # F Major
        ])

        self.tension_transition_matrix = np.array([
            [0.0, 0.5, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],  # G Major
            [0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.0, 0.0],  # C Major
            [0.25, 0.0, 0.0, 0.5, 0.0, 0.25, 0.0, 0.0, 0.0],# Am
            [0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.0, 0.0],  # F Major
            [0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.5, 0.0],  # E Major
            [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],  # Dm7
            [0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0],  # G7
            [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],  # Cmaj7
            [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0],  # A7
        ])


        ################################### SECON VERISON CHODS PROGRESSIOM

        self.LOW_calm_chords_mp3 = {
            'C': 'test3/C.mp3',
            'F': 'test3/F.mp3',
            'G': 'test3/G.mp3',
            'Am': 'test3/Am.mp3',
            'Dm': 'test3/Dm.mp3',
            'Em': 'test3/Em.mp3',
            'A': 'test3/A.mp3',
        }

        self.TURBO_high_tension_chords_mp3 = {
            'Am': 'test3/Am.mp3',
            'G': 'test3/G.mp3',
            'F': 'test3/F.mp3',
            'C': 'test3/C.mp3',
            'E': 'test3/E.mp3',
            'Bb': 'test3/Bb.mp3',
            'Ab': 'test3/Ab.mp3',
            'Cm': 'test3/Cm.mp3',
            'Dm': 'test3/Dm.mp3'
        }

        self.LOW_calm_transition_matrix = np.array([
            [0.0, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1],  # C
            [0.5, 0.0, 0.4, 0.1, 0.0, 0.0, 0.0],  # F
            [0.3, 0.0, 0.0, 0.2, 0.2, 0.0, 0.3],  # G
            [0.3, 0.1, 0.3, 0.0, 0.3, 0.0, 0.0],  # Am
            [0.3, 0.0, 0.7, 0.0, 0.0, 0.0, 0.0],  # Dm
            [0.3, 0.3, 0.4, 0.0, 0.0, 0.0, 0.0],  # Em
            [0.3, 0.3, 0.4, 0.0, 0.0, 0.0, 0.0]   # A
        ])

        self.TURBO_tension_transition_matrix = np.array([
            [0.1, 0.3, 0.2, 0.1, 0.1, 0.0, 0.0, 0.0, 0.2],  # Am
            [0.2, 0.1, 0.2, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1],  # G
            [0.2, 0.2, 0.0, 0.3, 0.0, 0.1, 0.0, 0.0, 0.2],  # F
            [0.0, 0.3, 0.3, 0.1, 0.0, 0.2, 0.0, 0.1, 0.0],  # C
            [0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0],  # E
            [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],  # Bb
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0],  # Ab
            [0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],  # Cm
            [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]   # Dm
        ])

        self.LOW_calm_chords = ['C', 'F', 'G', 'Am', 'Dm', 'Em', 'A']
        self.TURBO_tension_chords = ['Am', 'G', 'F', 'C', 'E', 'Bb', 'Ab', 'Cm', 'Dm']
        #################################################################################


        self.calm_chords = ['C Major', 'Dm7', 'G7', 'Cmaj7', 'Am', 'Dm', 'G Major', 'F Major']
        self.tension_chords = ['G Major', 'C Major', 'Am', 'F Major', 'E Major', 'Dm7', 'G7', 'Cmaj7', 'A7']

        self.channel1 = pygame.mixer.Channel(0)
        self.channel2 = pygame.mixer.Channel(1)

        self.current_chord_index = 0
        self.current_channel = self.channel1
        
    
    def get_next_chord(self, current_index, transition_matrix):
        probabilities = transition_matrix[current_index]
        next_index = np.random.choice(len(probabilities), p=probabilities)
        return next_index

    def play_chord(self, channel, chord_mp3):
        channel.play(pygame.mixer.Sound(chord_mp3))

    def music_generator(self):
        current_time = pygame.time.get_ticks()
        #print(self.next_time, current_time)
        if current_time >= self.next_time:
            if self.game_state == 'battle':
                if self.is_calm:
                    self.is_calm = False
                    self.current_chord_index = 0  # Start with the first tension chord
                next_chord_index = self.get_next_chord(self.current_chord_index, self.TURBO_tension_transition_matrix)
                self.play_chord(self.current_channel, self.TURBO_high_tension_chords_mp3[self.TURBO_tension_chords[next_chord_index]])
            elif self.game_state == 'close_to_enemy':
                if self.is_calm:
                    self.is_calm = False
                    self.current_chord_index = 0  # Start with the first tension chord
                next_chord_index = self.get_next_chord(self.current_chord_index, self.tension_transition_matrix )
                self.play_chord(self.current_channel, self.high_tension_chords_mp3[self.tension_chords[next_chord_index]])
            else:
                if not self.is_calm:
                    self.is_calm = True
                    self.current_chord_index = 0  # Start with the first calm chord
                next_chord_index = self.get_next_chord(self.current_chord_index, self.calm_transition_matrix)
                self.play_chord(self.current_channel, self.calm_chords_mp3[self.calm_chords[next_chord_index]])
            
            self.current_chord_index = next_chord_index

                # Switch channels
            self.current_channel = self.channel2 if self.current_channel == self.channel1 else self.channel1

            if self.game_state == 'battle' and self.player.current_health <= 400:
                self.next_time = current_time + 300
            elif self.game_state == 'close_to_enemy':   
                self.next_time = current_time + 450
            elif self.game_state == 'battle' :  
                self.next_time = current_time + 400
            else:
                self.next_time = current_time + 500

            #print(self.game_state)
            

    def check_state(self):
        if self.current_state != self.game_state:
            if self.music:
                self.music.fadeout(self.fade_duration)
            
            self.music = self.sounds[self.game_state]
            self.music.play(loops=-1)
            self.music.set_volume(0)  # Start silent and fade in
            self.is_fading = True
            self.fade_start_time = pygame.time.get_ticks()
            self.current_state = self.game_state


    def update_volume(self):
        if self.is_fading:
            elapsed_time = pygame.time.get_ticks() - self.fade_start_time
            fraction = min(elapsed_time / self.fade_duration, 1.0)

            new_volume = fraction * 0.8  # Assuming max volume is 0.8
            self.music.set_volume(new_volume)

            if elapsed_time >= self.fade_duration:
                self.is_fading = False
                self.music.set_volume(0.8)  # Ensure volume is set to full after fade-in completes



    def bullet_enemy_collision(self):
        if self.spell_group:
            for spell in self.spell_group:
                coll = pygame.sprite.spritecollide(spell, self.enemy_group, False)
                if coll:
                    for enemy in coll:
                        enemy.health -= 101
                        #print(enemy.health)
                    spell.kill()

    def spell_player_collision(self):
        if self.enemy_spell_group:
            for spell in self.enemy_spell_group:
                coll = pygame.sprite.spritecollide(spell, self.player_group, False)
                if coll:
                    self.player.current_health -= 200
                    spell.kill()

    def sword_enemy_collision(self):
        if self.sword:
            coll = pygame.sprite.spritecollide(self.sword, self.enemy_group, False)
            if coll:
                for enemy in coll:
                    enemy.kill()
                self.player.hide_sword()

    def player_potion_collisons(self):
        coll = pygame.sprite.spritecollide(self.player, self.potion_group, False)
        if coll:
            for potion in coll:
                if potion.type == 'mana':
                    self.player.get_mana(potion.value)
                else:
                    self.player.get_health(potion.value)

                potion.kill()

    def player_enemy_collisons(self):
        coll = pygame.sprite.spritecollide(self.player, self.enemy_group, False)
        if coll:
            for enemy in coll:
                self.player.damage(enemy.attack_damage)

                enemy.kill()

    def take_key(self):
        if self.player.rect.colliderect(self.key):
            self.key.kill()
            self.have_key = True

    def collide_end(self):
        if self.player.rect.colliderect(self.end_level) and self.have_key == True:
            if self.number_of_level <= self.level_number +1:
                self.end_game = True
                return
            else:    
                self.level_number += 1
                for enemy in self.end_group:
                    enemy.kill()

                self.game_state = 'exploration'
                self.is_calm = True
                self.have_key = False
                self.key_group.empty()
                self.all_sprites.empty()
                self.block_group.empty()
                self.enemy_group.empty()
                self.player_group.empty()
                self.enemy_spell_group.empty()
                self.potion_group.empty
                self.end_group.empty()
                self.sprite_group.empty()
                if self.important_table[2] != True:
                    self.music.stop()

                self.next_level()

    def get_mouse_direciton(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(W/2, H/2)
        self.player_direction = (mouse_pos - player_pos).normalize()

    def get_distance_to_enemy(self):
        self.enemy_dict = {}
        for enemy in self.enemy_group:
            distance = ((self.player.rect.centerx - enemy.rect.centerx)**2 + (self.player.rect.centery - enemy.rect.centery)**2)**(1/2)
            self.enemy_dict[enemy] = distance


    def update_game_state(self):
        if self.enemy_dict:
            #print(min(self.enemy_dict.values()))
            if min(self.enemy_dict.values()) < 400 and min(self.enemy_dict.values()) > 200:
                self.game_state = 'close_to_enemy'
            elif min(self.enemy_dict.values()) <= 200:
                self.game_state = 'battle'
            else:
                self.game_state = 'exploration'
        else:
            self.game_state = 'exploration'
        
        


    def magic_attack(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_attack_time > self.attack_cooldown and self.player.current_mana >= 100:
                pos = self.player.rect.center + self.player_direction * 20
                spell = Spell(pos, self.player_direction, self.sprite_group, self.block_group)
                self.spell_group.add(spell)
                self.player.usage(100)
                self.last_attack_time = current_time
    
    def sword_attack(self):
        self.sword = Sword(self.player, [self.sprite_group])

    def hide_sword(self):
        if self.sword:
            self.sword.kill()
            self.sword = None 
        self.sword = None 

    def next_level(self):
        self.level_date = level_date_tabel[self.level_number]
        self.setup_level(self.level_date)
        self.sprite_group.back = pygame.image.load(level_map_table[self.level_number]).convert()


    def update(self):
        self.get_distance_to_enemy()
        self.get_mouse_direciton()
        self.update_game_state()
        self.bullet_enemy_collision()
        self.spell_player_collision()
        self.sword_enemy_collision()
        self.player_potion_collisons()
        self.player_enemy_collisons()
        self.take_key()
        if self.important_table[1] == True:
            self.check_state()
            self.update_volume()
        elif self.important_table[2] == True:
            self.music_generator()

        self.magic_attack()
        #self.block_group.draw(self.screen)
        #self.player_group.draw(self.screen)
        #self.end_group.draw(self.screen)
        if self.sword: 
            self.sword.update()
        

        #print(self.have_key)
        self.sprite_group.update()
        self.sprite_group.custom_draw(self.player)
        #self.player.update() -> self.sprite_group.update() już to wykonuje
        self.player.health_bar_logic()
        self.player.mana_bar_logic()
        self.collide_end()
        if self.end_game == True or self.player.is_dead == True:
            if self.important_table[2] != True:
                self.music.stop()

            return -1

class Allsprites(pygame.sprite.Group):
    def __init__(self, lev_number):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.back = pygame.image.load(level_map_table[lev_number]).convert()
        self.back_rect = self.back.get_rect(topleft = (0,0))
        
    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        back_offset = self.back_rect.topleft - self.offset
        self.display_surface.blit(self.back,back_offset)

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)