import pygame.font

class Price_Button():

    def __init__(self,ai_settings,screen,ship):
        self.screen = screen
        
        self.price_width, self.price_height = 100,25
        self.price_color = (255,140,0)

        self.font = pygame.font.SysFont(None,30)

        self.price_rect = pygame.Rect(0,0,self.price_width,self.price_height)
        self.price_rect.bottom = ship.rect.top
        self.price_rect.centerx = ship.rect.centerx

        self.ship = ship
        
        
    def prep_msg(self):
        self.price_str = str(self.ship.price)
        self.price_text_color = self.ship.price_text_color
        self.price_image = self.font.render(self.price_str,True,self.price_text_color)
        self.price_image_rect = self.price_image.get_rect()
        self.price_image_rect.center = self.price_rect.center

    def draw_price_button(self):
        if self.ship.visible:
            self.prep_msg()
            self.screen.fill(self.price_color,self.price_rect)
            self.screen.blit(self.price_image,self.price_image_rect)
