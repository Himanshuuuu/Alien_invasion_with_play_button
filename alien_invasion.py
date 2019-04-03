import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
 
def run_game():
    pygame.init()
    ai_settings = Settings()
 
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
 
    #ship.py make a ship
    ship = Ship(ai_settings, screen)
 
    # make a group to store bullets and group of aliens
    bullets = Group()
    aliens = Group()
 
    # create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
 
 
    # make an alien
    alien = Alien(ai_settings,screen)
 
    while True:
        
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
               bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
 
        print(len(bullets))        
 
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
         play_button)
 
run_game()