import pygame
import random
from time import sleep

class Ship23():

    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("22.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.msg = "BUY"
        self.price = 2222
        self.price_text_color = (0,255,0)

        self.visible = True
        self.up = True
        self.buy = False
        self.time = 0
        self.max_money = 0

        self.rect.top = 80
        self.rect.right = self.screen_rect.right-200

    def check_buy(self):
        
        
        self.max_money = max(self.ai_settings.money,self.max_money)


        if self.max_money < 2200:
            self.visible = False
        
        if self.buy:
            self.visible = True
            self.msg = "SELL"
            
            if self.price <= 1700:
                self.up = True
                self.price_text_color = (0,255,0)
                
        else:
            self.msg = "BUY"

    def price_up(self):
        r = random.uniform(0,1)

        if r < 0.5 :
            self.price += 50
        else:
            self.price += 60

    def price_down(self):
        if self.price > 1900:
            r = random.uniform(0,1)

            if r < 0.5 :
                self.price -= 70
            else:
                self.price -= 80
        else:
            r = random.randint(150,400)
            self.price -= r

        if self.price < 1700 and not self.buy:
            self.visible = False



    def price_change(self):
        if self.price <= 2600 and self.up:
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
        self.price = 2200
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
            if self.time > 45:
                self.again()


