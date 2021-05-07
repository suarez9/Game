import pygame.font
from time import sleep
import sys



class Scoreboard():

    def __init__(self,ai_settings,screen):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.ai_settings = ai_settings

        self.text_color = (0,0,255)
        self.color = (0,255,0)
        self.font = pygame.font.SysFont(None,48)
        self.font2 = pygame.font.SysFont(None,35)
        self.font3 = pygame.font.SysFont(None,100)

        self.time = 0

        self.no_money = "LACK OF MONEY"
        self.win = "YOU WIN!"
        self.prep_no_money()
        self.prep_win()

    def prep_win(self):
        self.win_color = (255,0,0)
        self.win_back_color = (100,100,100)
        self.win_image = self.font3.render(self.win,True,self.win_color,self.win_back_color)

        self.win_rect = self.win_image.get_rect()
        self.win_rect.center = self.screen_rect.center

    def prep_score(self):

        score_str = str(self.ai_settings.money)
        self.score_image = self.font.render(score_str,True,self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.center = self.screen_rect.center 
        self.score_rect.bottom = 450
        
    def prep_no_money(self):
        
        self.no_money_image = self.font2.render(self.no_money,True,self.color)
        self.no_money_rect = self.no_money_image.get_rect()
        self.no_money_rect.centerx = self.screen_rect.centerx
        self.no_money_rect.top = 460

    def show_score(self):
        self.prep_score()
        self.screen.blit(self.score_image,self.score_rect)

    def show_not_enough_money(self):
        self.screen.blit(self.no_money_image,self.no_money_rect)

    def show_win(self):
        self.screen.blit(self.win_image,self.win_rect)
        pygame.display.flip()
        sleep(3)
        sys.exit()




        
