import time
from pokemon_factory import PokemonFactory
import pygame
from battle import draw_battle
from start import start_screen

pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Pokemon Remake")

def main():
    running = True
    clock = pygame.time.Clock()
    start_time = time.time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate the frame index for animation
        frame = int((time.time() - start_time) * 10)  # Adjust multiplier as needed

        player_id, opponent_id = start_screen(screen)

        # Example Pokémon objects (replace with your factory or actual Pokémon instances)
        player_pokemon = PokemonFactory.create_pokemon(player_id)
        opponent_pokemon = PokemonFactory.create_pokemon(opponent_id)
            
        # Draw the scene
        draw_battle(screen, "grassland", "day", player_pokemon, opponent_pokemon, frame)

        # Flip the display
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
