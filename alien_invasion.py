import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Control all method for the game and its behavior"""
    def __init__(self):
        """initialize the game and set game resources"""
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.display_width = self.screen.get_rect().width
        # self.settings.display_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.display_height, self.settings.display_width))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Run the main loop for the game"""
        while True:
            self._check_events()
            #update the ship imagne
            self.ship.update()
            #update the bullet which is drawn by pygame.draw.rect
            self.bullets.update()
            self._update_screen()

    def _check_events(self):
        #Update screen from the input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                #Check for the key press
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
                #check of key release
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self,event):
                #check for the right arrow key
        if event.key == pygame.K_RIGHT:
            #update the flag for moving
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #update the flag for moving
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            

    def _check_keyup_event(self,event):
        #check for the right arrow key
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        #check for the left arrow key
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Make a bullet and add to the group"""
        new_bullet = Bullet(self) 
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        #Draw the ship on screen
        self.ship.blitme()
        #get the bullets from the group and draw them
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Draw the most recent of the screen.
        pygame.display.flip()
         

if __name__ == '__main__':
    """Make the game instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()
