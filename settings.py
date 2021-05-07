import pygame

class Settings():

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.background = pygame.image.load("back.jpg")

        self.money = 100
