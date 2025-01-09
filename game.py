# Pokemon Factory class will be responsible for creating Pokemon objects.
from pokemon_factory import PokemonFactory
# Pygame is a library that will be used to create the game window, as well as to display images and animations and play sound.
import pygame
from battle_view import load_gif, draw_background

# Set up pygame screen to fit the user's screen. He can resize the window, and full screen.
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Pokemon Remake")

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_background(screen, "grassland", "day")
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()