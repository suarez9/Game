import pygame
import random
from time import sleep

class Ship11():

    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load("11.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.msg = "BUY"
        self.price = 20
        self.price_text_color = (0,255,0)

        self.visible = True
        self.up = True
        self.buy = False
        self.time = 0

        self.rect.bottom = self.screen_rect.bottom - 20
        self.rect.left = 155

    def check_buy(self):
        
        if self.buy:
            self.visible = True
            self.msg = "SELL"
            
            if self.price <= 10:
                self.up = True
                self.price_text_color = (0,255,0)
                
        else:
            self.msg = "BUY"

    def price_up(self):
        r = random.uniform(0,1)

        if r < 0.5 :
            self.price += 1
        else:
            self.price += 2

    def price_down(self):
        if self.price > 14:
            r = random.uniform(0,1)

            if r < 0.5 :
                self.price -= 3
            else:
                self.price -= 4
        else:
            r = random.randint(1,10)
            self.price -= r

        if self.price < 10 and not self.buy:
            self.visible = False

    def price_change(self):
        if self.price <= 40 and self.up:
            self.price_up()
            sleep(0.07)
        else:
            r = random.uniform(0,1)

            if r < 0.7 and self.up :
                self.price_up()
                sleep(0.07)
                r = random.uniform(0,1)
            else:
                self.up = False
                self.price_text_color = (255,0,0)

        if not self.up and self.visible:
            self.price_down()
            sleep(0.07)

    def again(self):
        self.price = 18
        self.visible = True
        self.time = 0
        self.up = True
        self.price_text_color = (0,255,0)
        
        self.blitme()

    def blitme(self):
        self.check_buy()
        if self.visible:
            self.price_change()
            if self.visible:
                self.screen.blit(self.image,self.rect)
        else:
            self.time += 1
            if self.time > 25:
                self.again()






                
