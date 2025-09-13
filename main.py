import sys
import asyncio
import pygame
from time import sleep
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from stars import Star
from random import randint
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Control all method for the game and its behavior"""
    def __init__(self):
        """initialize the game and set game resources"""
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # SWITCH B/T FULL SCREEN TO CUSTAMISEABLE 
        self.screen = pygame.display.set_mode((self.settings.display_width, self.settings.display_height))
        self.settings.display_width = self.screen.get_rect().width
        self.settings.display_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self._create_fleet()
        self._create_stars()
        self.play_button = Button(self, "Play")
        self.sb = Scoreboard(self)
        # self.fire = False

    async def run_game(self):
        """Run the main loop for the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                #update the ship imagne
                self.ship.update()
                #Move the aliens
                self._update_alien()
                #update the bullet which is drawn by pygame.draw.rect
                self._update_bullets()
            self._update_screen()
            await asyncio.sleep(0)

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
                #check the mouse button press and position
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_pos(mouse_pos)

    def _check_mouse_pos(self, pos):
        """Start the game when clicked on play button"""
        if self.play_button.rect.collidepoint(pos) and not self.stats.game_active:
            self.settings.initialise_dynamic_settings()
            self.stats.game_active = True
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self.ship.center_ship()
            #make the cursor disapper
            pygame.mouse.set_visible(False)

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

    def _create_alien(self, alien_number, row_number):
        """Make the alien ship at differet location"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = (alien_width) + ((2*alien_number)*alien_width)
        alien.rect.x = alien.x
        alien.rect.y = (alien_height) + (2*row_number)*alien_height
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create the fleet of aliens from create alien"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.screen.get_rect().width - (alien_width)
        number_aliens_x = available_space_x//(2*alien_width)
        ship_height = self.ship.rect.height
        available_space_y = self.screen.get_rect().height - 3*alien_height - ship_height
        number_rows = available_space_y//(2*alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Check wether the alien has reached the left or right edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.alien_direction *= -1

    def _update_alien(self):
        """Update the coordinates of the aliens"""
        self._check_fleet_edges()
        self.aliens.update()
        #look for the alien and ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #Check alien reached at bottom
        self._check_alien_bottom()

    def _ship_hit(self):
        if self.stats.ship_left > 0:
            self._update_screen()
            #decrease the no. of ship
            self.stats.ship_left -= 1
            #get rid of the aliens and bullets
            self.aliens.empty()
            self.sb.prep_ships()
            self.bullets.empty()
            #Pause the game and center the ship
            self._create_fleet()
            self.ship.center_ship()
            #Pause the ship 
            sleep(1.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_alien_bottom(self):
        """Look for the alien to reach the bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat as the ship get hit.
                self._ship_hit()
                break

    def _fire_bullet(self):
        """Make a bullet and add to the group"""
        if len(self.bullets) < self.settings.allowed_bullets and self.stats.game_active:
            new_bullet = Bullet(self) 
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the bullet position and remove the bullets that had 
            crossed the top of screen"""
        #update
        self.bullets.update()
        #remove
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        #check for the bullet tha have hit the alien and remove them
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points*(len(aliens))
            self.sb.prep_score()
            self.sb.check_high_score()
        #repopulate the fleet
        if not self.aliens:
            """remove the remaining bullets and creating new fleet"""
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _create_stars(self):
        if self.settings.night_mode:
            for num in range(self.settings.stars):
                star = Star(self)
                star.rect.x = randint(0, self.screen.get_rect().width)
                star.rect.y = randint(0, self.screen.get_rect().height)
                self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # if self.settings.night_mode:
        self.stars.draw(self.screen)
        #Draw the ship on screen
        self.ship.blitme()
        #get the bullets from the group and draw them
        self.aliens.draw(self.screen)
        self.sb.show_score()
        #Draw the play button when the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Draw the most recent of the screen.
        pygame.display.flip()
         

if __name__ == '__main__':
    """Make the game instance and run the game."""
    ai = AlienInvasion()
    asyncio.run(ai.run_game())
