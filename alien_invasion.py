import sys
import pygame

class AlienInvasion:
    """Control all method for the game and its behavior"""
    def __init__(self):
        """initialize the game and set game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1250, 615))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Run the main loop for the game"""
        while True:
            #Update screen from the input.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Drow the most recent of the screen.
            pygame.display.flip()

if __name__ == '__main__':
    """Make the game instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()



    