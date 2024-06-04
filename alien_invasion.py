import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Control all method for the game and its behavior"""
    def __init__(self):
        """initialize the game and set game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.display_height, self.settings.display_width))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Run the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        #Update screen from the input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                #Check for the key press
            elif event.type == pygame.KEYDOWN:
                #check for the right arrow key
                if event.key == pygame.K_RIGHT:
                    #update the flag for moving
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    #update the flag for moving
                    self.ship.moving_left = True
                #check of key release
            elif event.type == pygame.KEYUP:
                #check for the right arrow key
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                #check for the left arrow key
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        #Drow the ship on screen
        self.ship.blitme()
        #update the plane imagne
        self.ship.update()
        #Drow the most recent of the screen.
        pygame.display.flip()
         

if __name__ == '__main__':
    """Make the game instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()
