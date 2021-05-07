import pygame
import pygame.font
from time import sleep
import sys
from settings import Settings
from ship1 import Ship1
from ship22 import Ship22
from ship23 import Ship23
from ship24 import Ship24
from ship25 import Ship25
from ship26 import Ship26
from ship6 import Ship6
from ship7 import Ship7
from ship8 import Ship8
from ship9 import Ship9
from ship10 import Ship10
from ship11 import Ship11
from ship12 import Ship12
from ship13 import Ship13
from introduction import Introduction
import game_functions as gf
from buy_button import Buy_Button
from price_button import Price_Button
from scoreboard import Scoreboard


# -*- coding: UTF-8 -*-


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Ship Seller")

    sb = Scoreboard(ai_settings, screen)
    introduct = Introduction(screen)

    ship1 = Ship1(screen)
    buy_button1 = Buy_Button(ai_settings, screen, ship1)
    price_button1 = Price_Button(ai_settings, screen, ship1)

    ship10 = Ship10(screen)
    ship11 = Ship11(screen)
    ship12 = Ship12(screen)
    ship13 = Ship13(screen)
    buy_button10 = Buy_Button(ai_settings, screen, ship10)
    price_button10 = Price_Button(ai_settings, screen, ship10)
    buy_button11 = Buy_Button(ai_settings, screen, ship11)
    price_button11 = Price_Button(ai_settings, screen, ship11)
    buy_button12 = Buy_Button(ai_settings, screen, ship12)
    price_button12 = Price_Button(ai_settings, screen, ship12)
    buy_button13 = Buy_Button(ai_settings, screen, ship13)
    price_button13 = Price_Button(ai_settings, screen, ship13)

    ship6 = Ship6(ai_settings, screen)
    ship7 = Ship7(ai_settings, screen)
    ship8 = Ship8(ai_settings, screen)
    ship9 = Ship9(ai_settings, screen)
    buy_button6 = Buy_Button(ai_settings, screen, ship6)
    price_button6 = Price_Button(ai_settings, screen, ship6)
    buy_button7 = Buy_Button(ai_settings, screen, ship7)
    price_button7 = Price_Button(ai_settings, screen, ship7)
    buy_button8 = Buy_Button(ai_settings, screen, ship8)
    price_button8 = Price_Button(ai_settings, screen, ship8)
    buy_button9 = Buy_Button(ai_settings, screen, ship9)
    price_button9 = Price_Button(ai_settings, screen, ship9)

    ship22 = Ship22(ai_settings, screen)
    ship23 = Ship23(ai_settings, screen)
    ship24 = Ship24(ai_settings, screen)
    ship25 = Ship25(ai_settings, screen)
    ship26 = Ship26(ai_settings, screen)
    buy_button22 = Buy_Button(ai_settings, screen, ship22)
    price_button22 = Price_Button(ai_settings, screen, ship22)
    buy_button23 = Buy_Button(ai_settings, screen, ship23)
    price_button23 = Price_Button(ai_settings, screen, ship23)
    buy_button24 = Buy_Button(ai_settings, screen, ship24)
    price_button24 = Price_Button(ai_settings, screen, ship24)
    buy_button25 = Buy_Button(ai_settings, screen, ship25)
    price_button25 = Price_Button(ai_settings, screen, ship25)
    buy_button26 = Buy_Button(ai_settings, screen, ship26)
    price_button26 = Price_Button(ai_settings, screen, ship26)

    while True:

        if introduct.start:
            gf.check_events(ai_settings, sb, ship1, buy_button1,
                            ship6, buy_button6, ship7, buy_button7, ship8, buy_button8, ship9, buy_button9,
                            ship10, buy_button10, ship11, buy_button11, ship12, buy_button12, ship13, buy_button13,
                            ship22, buy_button22, ship23, buy_button23, ship24, buy_button24, ship25, buy_button25,
                            ship26, buy_button26)
            gf.update_screen(ai_settings, screen, sb, ship1, buy_button1, price_button1,
                             ship6, buy_button6, price_button6, ship7, buy_button7, price_button7,
                             ship8, buy_button8, price_button8, ship9, buy_button9, price_button9,
                             ship10, buy_button10, price_button10, ship11, buy_button11, price_button11,
                             ship12, buy_button12, price_button12, ship13, buy_button13, price_button13,
                             ship22, buy_button22, price_button22, ship23, buy_button23, price_button23,
                             ship24, buy_button24, price_button24, ship25, buy_button25, price_button25,
                             ship26, buy_button26, price_button26)
        else:
            introduct.down_play()


run_game()
