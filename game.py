from battle_view import setup_battle_screen
from pokemon_factory import PokemonFactory
import pygame

# Set up pygame screen to fit the user's screen. He can resize the window, and full screen.
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Pokemon Remake")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # Update display


    pygame.display.flip()
pygame.quit()