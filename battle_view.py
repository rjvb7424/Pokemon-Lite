from PIL import Image
import pygame
import time

# Loading gifs is not a native feature of pygame, so we need to use PIL to load the gif and convert it to a pygame surface.
# This function will load a gif and return a list of pygame surfaces, one for each frame.
def load_gif(gif_path):
    frames = []
    gif = Image.open(gif_path)
    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_image = gif.convert("RGBA")
        frame_surface = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
        frames.append(frame_surface)
    return frames

def draw_background(screen, location, time_of_day):
    # Load the appropriate background image based on the location and time of day.
    if location == "grassland" and time_of_day == "day":
        wallpaper_sprite = "battle sprites/wallpaper/grassland_day.png"
        bases_sprite = "battle sprites/bases/grass_day.png"
    # All battle backgrounds are 256 by 146 pixels.
    # We need to scale them up to fit the screen.
    wallpaper = pygame.transform.scale(pygame.image.load(wallpaper_sprite), (screen.get_width(), screen.get_height()))
    bases = pygame.transform.scale(pygame.image.load(bases_sprite), (screen.get_width(), screen.get_height()))
    # Then after scaling we can draw the background on the screen.
    screen.blit(wallpaper, (0, 0))
    screen.blit(bases, (0, 0))

def draw_player_pokemon(screen, pokemon, x, y, frame):
    # Load the player's pokemon gif frames.
    player_frames = load_gif(pokemon.back_sprite)
    # Get the current frame to display.
    player_sprite = player_frames[frame % len(player_frames)]
    # Scale the sprite to fit the screen.
    scaled_sprite = pygame.transform.scale(player_sprite, (screen.get_width(), screen.get_height()))
    screen.blit(scaled_sprite, (x, y))

def draw_opponent_pokemon(screen, pokemon, x, y, frame):
    # Load the opponent's pokemon gif frames.
    opponent_frames = load_gif(pokemon.front_sprite)
    # Get the current frame to display.
    opponent_sprite = opponent_frames[frame % len(opponent_frames)]
    # Scale the sprite to fit the screen
    scaled_sprite = pygame.transform.scale(opponent_sprite, (screen.get_width(), screen.get_height()))
    screen.blit(scaled_sprite, (x, y))

def draw_battle(screen, location, time_of_day, player_pokemon, opponent_pokemon, frame):
    # Draw the background
    draw_background(screen, location, time_of_day)
        
    width = screen.get_width()
    height = screen.get_height()

    player_x = int((3 * width) / 4)
    player_y = int((3 * height) / 4)
    opponent_x = int((width / 4))
    opponent_y = int((width / 4))

    # Draw the player's pokemon
    draw_player_pokemon(screen, player_pokemon, player_x, player_y, frame)
        
    # Draw the opponent's pokemon
    draw_opponent_pokemon(screen, opponent_pokemon, opponent_x, opponent_y, frame)