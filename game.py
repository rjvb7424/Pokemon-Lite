import time
from pokemon_factory import PokemonFactory
import pygame
from battle_view import draw_battle

# Set up pygame screen to fit the user's screen. The user can resize the window or go full screen.
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Pokemon Remake")

def main():
    # Game variables
    running = True
    clock = pygame.time.Clock()  # To control frame rate
    start_time = time.time()

    # Example Pokémon objects (replace with actual factory or Pokémon instances)
    player_pokemon = PokemonFactory.create_pokemon(25)
    opponent_pokemon = PokemonFactory.create_pokemon(6)

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate the frame (e.g., change every 100 ms)
        frame = int((time.time() - start_time) * 10)  # Adjust the multiplier for speed

        draw_battle(screen, "grassland", "day", player_pokemon, opponent_pokemon, frame)

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
