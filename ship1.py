import pygame
import random
from time import sleep

class Ship1():

    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load("44.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.msg = "BUY"
        self.price = 20000
        self.price_text_color = (0,255,0)

        
        self.up = True
        self.visible = True

        self.rect.center = self.screen_rect.center

        

    

    def price_up(self):
        r = random.randint(100,300)

        self.price += r

    def price_down(self):
        r = random.randint(100,300)

        self.price -= r

    def price_change(self):
        if self.price <= 22000 and self.up:
            self.price_up()
            sleep(0.06)
        else:
            r = random.uniform(0,1)

            if r < 0.7 and self.up :
                self.price_up()
                sleep(0.06)
                r = random.uniform(0,1)
            else:
                self.up = False
                self.price_text_color = (255,0,0)

        if not self.up:
            self.price_down()
            sleep(0.1)

    def change(self):
        if self.price < 18000:
            self.price_text_color = (0,255,0)
            self.up = True

    def blitme(self):
        self.price_change()
        self.change()
        self.screen.blit(self.image,self.rect)







                
        
