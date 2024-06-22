import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    """Represent the single alien in the fleet"""
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        if self.settings.night_mode:
            self.image = pygame.image.load('Images/alien_ship.png')
        else:
            self.image = pygame.image.load('Images/alien_ship02.bmp')
        self.rect = self.image.get_rect()
        #set the position of the alien to the top left corner with space equal to height and width
        self.rect.x =  self.rect.width
        self.rect.y =  self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """Alien reached the edge or not"""
        screen_rect = self.screen.get_rect()
        if self.rect.left <= 0 or self.rect.right >= screen_rect.right :
            return True
        
    def check_change(self, l):
        """rendomly change the direction of alien"""
        screen_rect = self.screen.get_rect()
        q_3 = (screen_rect.right)*5//8
        q_1 = (screen_rect.right)*3//8
        num = randint (q_3, screen_rect.right)
        num_l = randint (10, q_1)
        if self.rect.left == num and l == 0:
            return True
        if self.rect.left == num_l and l == 1:
            return True


    def update(self, num):
        """Move the alien to the right"""
        if num == 1:
            self.x -= (self.settings.alien_speed)
            self.rect.x = self.x
        else:
            self.x += (self.settings.alien_speed)
            self.rect.x = self.x


    
    