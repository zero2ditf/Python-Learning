import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Shooter")

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)

        gf.update_screen(ai_settings, screen, ship)
        for event in pygame.event.get():
            ship.update()
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()


run_game()
