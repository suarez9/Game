import pygame.font

class Buy_Button():

    def __init__(self,ai_settings,screen,ship):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.ship = ship

        self.buy_width, self.buy_height = 50,40
        self.buy_color = (255,255,255)
        self.buy_text_color = (255,0,0)

        self.msg = ship.msg
        self.font = pygame.font.SysFont(None,30)
        
        self.buy_rect = pygame.Rect(0,0,self.buy_width,self.buy_height)
        self.buy_rect.center = ship.rect.center
        

        self.prep_msg()

    def prep_msg(self):
        self.msg = self.ship.msg
        self.msg_image = self.font.render(self.msg,True,self.buy_text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.buy_rect.center

    def draw_buy_button(self):
        if self.ship.visible:
            self.prep_msg()
            self.screen.blit(self.msg_image,self.msg_image_rect)
