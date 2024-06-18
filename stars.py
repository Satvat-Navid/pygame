import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Stars in the sky"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # self.settings = ai_game.settings
        self.image = pygame.image.load('Images/star1.bmp')
        self.rect = self.image.get_rect()
