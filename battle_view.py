import pygame
import os
from PIL import Image

def load_gif_frames(gif_path):
    frames = []
    gif = Image.open(gif_path)
    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_image = gif.convert("RGBA")
        frame_data = frame_image.tobytes()
        frame_surface = pygame.image.fromstring(frame_data, frame_image.size, frame_image.mode)
        frames.append(frame_surface)
    return frames

def setup_battle_screen(player_pokemon, opponent_pokemon, wallpaper_path, bases_path):
    # Initialize Pygame
    pygame.init()

    # Set screen dimensions
    screen_width, screen_height = 256, 146
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Pokemon Battle")

    # Load images
    wallpaper = pygame.image.load(wallpaper_path)
    bases = pygame.image.load(bases_path)
    player_frames = load_gif_frames(player_pokemon.back_sprite)
    opponent_frames = load_gif_frames(opponent_pokemon.front_sprite)

    # Scale images to fit the screen
    wallpaper = pygame.transform.scale(wallpaper, (screen_width, screen_height))
    bases = pygame.transform.scale(bases, (screen_width, screen_height))
    player_frames = [pygame.transform.scale(frame, (int(screen_width * 0.25), int(screen_height * 0.25))) for frame in player_frames]
    opponent_frames = [pygame.transform.scale(frame, (int(screen_width * 0.25), int(screen_height * 0.25))) for frame in opponent_frames]

    # Frame indices
    player_frame_index = 0
    opponent_frame_index = 0

    # Frame update timing
    frame_duration = 100  # milliseconds
    last_update_time = pygame.time.get_ticks()

    # Main loop
    running = True
    while running:
        current_time = pygame.time.get_ticks()
        if current_time - last_update_time > frame_duration:
            player_frame_index = (player_frame_index + 1) % len(player_frames)
            opponent_frame_index = (opponent_frame_index + 1) % len(opponent_frames)
            last_update_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                wallpaper = pygame.transform.scale(wallpaper, (screen_width, screen_height))
                bases = pygame.transform.scale(bases, (screen_width, screen_height))
                player_frames = [pygame.transform.scale(frame, (int(screen_width * 0.25), int(screen_height * 0.25))) for frame in player_frames]
                opponent_frames = [pygame.transform.scale(frame, (int(screen_width * 0.25), int(screen_height * 0.25))) for frame in opponent_frames]

        # Draw images
        screen.blit(wallpaper, (0, 0))
        screen.blit(bases, (0, 0))
        screen.blit(player_frames[player_frame_index], (int(screen_width * 0.1), int(screen_height * 0.5)))
        screen.blit(opponent_frames[opponent_frame_index], (int(screen_width * 0.7), int(screen_height * 0.1)))

        # Update display
        pygame.display.flip()

    pygame.quit()