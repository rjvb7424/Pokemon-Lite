from PIL import Image
import pygame

def load_gif(gif_path):
    frames = []
    gif = Image.open(gif_path)
    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_image = gif.convert("RGBA")
        frame_surface = pygame.image.fromstring(
            frame_image.tobytes(),
            frame_image.size,
            frame_image.mode
        )
        frames.append(frame_surface)
    return frames

def draw_background(screen, location, time_of_day):
    if location == "grassland" and time_of_day == "day":
        wallpaper_sprite = "battle sprites/wallpaper/grassland_day.png"
        bases_sprite = "battle sprites/bases/grass_day.png"

    wallpaper = pygame.transform.scale(
        pygame.image.load(wallpaper_sprite),
        (screen.get_width(), screen.get_height())
    )
    bases = pygame.transform.scale(
        pygame.image.load(bases_sprite),
        (screen.get_width(), screen.get_height())
    )
    screen.blit(wallpaper, (0, 0))
    screen.blit(bases, (0, 0))

def draw_player_pokemon(screen, pokemon, base_x, base_y, frame):
    # Load the player's Pokémon frames
    player_frames = load_gif(pokemon.back_sprite)
    player_sprite = player_frames[frame % len(player_frames)]

    # Scale up the sprite
    original_size = player_sprite.get_size()
    scaled_sprite = pygame.transform.scale(
        player_sprite,
        (original_size[0] * 8, original_size[1] * 8)
    )
    
    # Position the bottom of the sprite at (base_x, base_y)
    sprite_rect = scaled_sprite.get_rect()
    sprite_rect.midbottom = (base_x, base_y)

    # Draw onto the screen
    screen.blit(scaled_sprite, sprite_rect)

def draw_opponent_pokemon(screen, pokemon, base_x, base_y, frame):
    # Load the opponent's Pokémon frames
    opponent_frames = load_gif(pokemon.front_sprite)
    opponent_sprite = opponent_frames[frame % len(opponent_frames)]

    # Scale up the sprite
    original_size = opponent_sprite.get_size()
    scaled_sprite = pygame.transform.scale(
        opponent_sprite,
        (original_size[0] * 8, original_size[1] * 8)
    )
    
    # Position the bottom of the sprite at (base_x, base_y)
    sprite_rect = scaled_sprite.get_rect()
    sprite_rect.midbottom = (base_x, base_y)

    # Draw onto the screen
    screen.blit(scaled_sprite, sprite_rect)

def draw_battle(screen, location, time_of_day, player_pokemon, opponent_pokemon, frame):
    # Draw the background
    draw_background(screen, location, time_of_day)
    
    # Get screen dimensions
    width = screen.get_width()
    height = screen.get_height()
    
    # Player Pokémon near bottom-left
    player_x = int(width * 0.25)
    player_y = int(height * 1.04)

    opponent_x = int(width * 0.75)
    opponent_y = int(height * 0.65)

    # Draw both Pokémon
    draw_player_pokemon(screen, player_pokemon, player_x, player_y, frame)
    draw_opponent_pokemon(screen, opponent_pokemon, opponent_x, opponent_y, frame)
