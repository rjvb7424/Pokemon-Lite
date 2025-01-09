from PIL import Image
import pygame

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
    # Thne after scaling we can draw the background on the screen.
    screen.blit(wallpaper, (0, 0))
    screen.blit(bases, (0, 0))