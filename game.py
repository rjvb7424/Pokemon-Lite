from pokemon import Pokemon
from PIL import Image, ImageSequence
import pygame
import sys

# Initialize Pygame
pygame.init()

# Initialize the mixer for sound
pygame.mixer.init()

# Load the sound file
  # Replace with your file path

# Play the sound


# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animated Sprite with Sound")

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Load the animated GIF using Pillow
index = 29
pokemon_instance = Pokemon(index=index, health_points= 3, attack= 3, defense= 9, special_attack= 3, special_defense= 3, speed= 3)  # Create an instance of the Pokemon class
gif_path = pokemon_instance.front_sprite  # Ensure the attribute is correctly referenced
gif_image = Image.open(gif_path)

sound_effect = pygame.mixer.Sound(f"cries/{index}.ogg")
sound_effect.play()

# Extract frames from the GIF
frames = []
for frame in ImageSequence.Iterator(gif_image):
    frame = frame.convert("RGBA")  # Ensure compatibility with Pygame
    pygame_image = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)

    # Scale up the frame (e.g., 4x bigger)
    scaled_frame = pygame.transform.scale(
        pygame_image, (frame.width * 4, frame.height * 4)  # Adjust scale factor
    )
    frames.append(scaled_frame)

# Get the rectangle for positioning
sprite_rect = frames[0].get_rect()
sprite_rect.center = (screen_width // 2, screen_height // 2)  # Center the sprite

# Game loop
running = True
frame_index = 0  # Track the current frame
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Example: Play sound on key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play sound when Space is pressed
                sound_effect.play()

    # Clear the screen with a background color
    screen.fill((30, 30, 30))  # Dark gray background

    # Draw the current frame of the GIF
    screen.blit(frames[frame_index], sprite_rect)

    # Update the frame index to create animation
    frame_index = (frame_index + 1) % len(frames)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to control GIF speed (adjust as needed)
    clock.tick(10)  # Adjust the frame rate for animation speed

# Quit Pygame
pygame.quit()
sys.exit()
