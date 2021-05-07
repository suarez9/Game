import sys
import pygame
from time import sleep

def check_events(ai_settings,sb,ship1,b1,
                 ship6,b6,ship7,b7,ship8,b8,ship9,b9,
                 ship10,b10,ship11,b11,ship12,b12,ship13,b13,
                 ship22,b22,ship23,b23,ship24,b24,ship25,b25,ship26,b26):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            win(ai_settings,b1,sb,ship1,mouse_x,mouse_y)
            
            check_buy(ai_settings,b6,sb,ship6,mouse_x,mouse_y)
            check_buy(ai_settings,b7,sb,ship7,mouse_x,mouse_y)
            check_buy(ai_settings,b8,sb,ship8,mouse_x,mouse_y)
            check_buy(ai_settings,b9,sb,ship9,mouse_x,mouse_y)

            check_buy(ai_settings,b10,sb,ship10,mouse_x,mouse_y)
            check_buy(ai_settings,b11,sb,ship11,mouse_x,mouse_y)
            check_buy(ai_settings,b12,sb,ship12,mouse_x,mouse_y)
            check_buy(ai_settings,b13,sb,ship13,mouse_x,mouse_y)

            check_buy(ai_settings,b22,sb,ship22,mouse_x,mouse_y)
            check_buy(ai_settings,b23,sb,ship23,mouse_x,mouse_y)
            check_buy(ai_settings,b24,sb,ship24,mouse_x,mouse_y)
            check_buy(ai_settings,b25,sb,ship25,mouse_x,mouse_y)
            check_buy(ai_settings,b26,sb,ship26,mouse_x,mouse_y)

def check_buy(ai_settings,buy_button,sb,ship,mouse_x, mouse_y):
    button_clicked = buy_button.buy_rect.collidepoint(mouse_x,mouse_y)

    if ship.visible and button_clicked:
        if ship.buy:
            ship.buy = False
            ship.visible = False
            ship.time = 0
            ai_settings.money += ship.price
        elif not ship.buy and ai_settings.money >= ship.price:
            ship.buy = True
            ai_settings.money -= ship.price

        elif not ship.buy and ai_settings.money < ship.price:
            sb.time = 2

def win(ai_settings,buy_button,sb,ship,mouse_x, mouse_y):
    button_clicked = buy_button.buy_rect.collidepoint(mouse_x,mouse_y)

    if ai_settings.money >= ship.price and button_clicked:
        sb.show_win()
    elif ai_settings.money < ship.price and button_clicked:
        sb.time = 2;
    
    
def show(ship,buy_button,price_button):
    ship.blitme()
    buy_button.draw_buy_button()
    price_button.draw_price_button()
            

def update_screen(ai_settings,screen,sb,
                  ship1,buy_button1,price_button1,
                  
                  ship6,buy_button6,price_button6,
                  ship7,buy_button7,price_button7,
                  ship8,buy_button8,price_button8,
                  ship9,buy_button9,price_button9,
                  
                  ship10,buy_button10,price_button10,
                  ship11,buy_button11,price_button11,
                  ship12,buy_button12,price_button12,
                  ship13,buy_button13,price_button13,

                  ship22,buy_button22,price_button22,
                  ship23,buy_button23,price_button23,
                  ship24,buy_button24,price_button24,
                  ship25,buy_button25,price_button25,
                  ship26,buy_button26,price_button26
                  ):

    
    screen.blit(ai_settings.background,(0,0))

    show(ship1,buy_button1,price_button1)
    
    show(ship6,buy_button6,price_button6)
    show(ship7,buy_button7,price_button7)
    show(ship8,buy_button8,price_button8)
    show(ship9,buy_button9,price_button9)
    
    show(ship10,buy_button10,price_button10)
    show(ship11,buy_button11,price_button11)
    show(ship12,buy_button12,price_button12)
    show(ship13,buy_button13,price_button13)

    show(ship22,buy_button22,price_button22)
    show(ship23,buy_button23,price_button23)
    show(ship24,buy_button24,price_button24)
    show(ship25,buy_button25,price_button25)
    show(ship26,buy_button26,price_button26)

    sb.show_score()
    if sb.time > 0:
        sb.show_not_enough_money()
        sb.time -= 1
    
    pygame.display.flip()





        
    
