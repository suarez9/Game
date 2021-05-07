import pygame
from time import sleep
import sys


# -*- coding: UTF-8 -*-

class Introduction():

    def __init__(self, screen):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.background = pygame.image.load("back.bmp")
        self.font1 = pygame.font.SysFont(None, 60)
        self.font2 = pygame.font.SysFont(None, 48)

        self.star = pygame.image.load("01.jpg")
        self.star_rect = self.star.get_rect()
        self.star_rect.centerx = self.screen_rect.centerx
        self.star_rect.top = 30

        self.text_color = (0, 255, 0)
        self.introduction = "BUY THE DEATH STAR!"
        self.play = "PLAY"
        self.start = False

        self.prep_msg()

    def prep_msg(self):
        self.introductionimage = self.font1.render(self.introduction, True, self.text_color)
        self.introductionimage_rect = self.introductionimage.get_rect()
        self.introductionimage_rect.center = self.screen_rect.center

        self.playimage = self.font2.render(self.play, True, self.text_color)
        self.playimage_rect = self.playimage.get_rect()
        self.playimage_rect.centerx = self.screen_rect.centerx
        self.playimage_rect.top = self.introductionimage_rect.bottom + 50

    def draw_back(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.star, self.star_rect)
        self.screen.blit(self.introductionimage, self.introductionimage_rect)
        self.screen.blit(self.playimage, self.playimage_rect)
        pygame.display.flip()

    def down_play(self):
        self.draw_back()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_clicked = self.playimage_rect.collidepoint(mouse_x, mouse_y)

                if button_clicked:
                    self.start = True

            elif event.type == pygame.QUIT:
                sys.exit()
