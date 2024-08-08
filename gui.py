import pygame
import sys
from config import *

class GUI:
    def __init__(self, screen, text_font):
        self.music_choice = None
        self.screen = screen
        self.running = True
        self.text_font = text_font
    
        self.button1 = Button('Play', (200,50), 400, 50, self.screen, self.text_font)
        self.button2 = Button('Sciezka 1', (200,140), 400, 50, self.screen, self.text_font)
        self.button3 = Button('Sciezka 2', (200,230), 400, 50, self.screen, self.text_font)
        self.button4 = Button('Sciezka 3', (200,320), 400, 50, self.screen, self.text_font)
        self.button5 = Button('Quit', (200,410), 400, 50, self.screen, self.text_font)

        self.buttons = [self.button2, self.button3, self.button4]

        self.music = pygame.mixer.Sound('linear/menu.mp3')
        self.music.set_volume(0.8)
        self.music.play(loops=-1)


    def main_menu(self):
        self.button1.all_in_one()
        self.button2.all_in_one()
        self.button3.all_in_one()
        self.button4.all_in_one()
        self.button5.all_in_one()

    def check_pressed_music(self):
        for button in self.buttons:
            if button.button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    for btn in self.buttons:
                        if btn != button:
                            btn.set_pressed(False)
                    button.set_pressed(True)
                    pygame.time.wait(200)

    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if self.button5.pressed:
                    sys.exit()
                if self.button1.pressed and any([self.button2.pressed,self.button3.pressed,self.button4.pressed]):
                    self.running = False
                    self.music.stop()
                    return [self.button2.pressed,self.button3.pressed,self.button4.pressed]

            self.screen.fill('black')
            self.main_menu()
            self.check_pressed_music()
            
            pygame.display.update()


class Button:
    def __init__(self, text_input, pos, width, height, screen, text_font):
        self.screen = screen
        self.button_rect = pygame.Rect(pos, (width, height))
        self.color = '#ffffff'
        self.text_input = text_input
        self.text_font = text_font
        self.pressed = False

        self.update_text_color()

    def update_text_color(self):
        if self.pressed:
            self.text = self.text_font.render(self.text_input, True, '#ff3300')  
        else:
            self.text = self.text_font.render(self.text_input, True, '#0000ff') 

        self.text_rect = self.text.get_rect(center=self.button_rect.center)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.button_rect)
        self.screen.blit(self.text, self.text_rect)

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = not self.pressed
                self.update_text_color()
                pygame.time.wait(200)

    def set_pressed(self, state):
        self.pressed = state
        self.update_text_color()

    def all_in_one(self):
        self.draw()
        self.is_pressed()