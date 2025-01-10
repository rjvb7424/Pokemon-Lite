import pygame
import time
from PIL import Image
from pokemon_factory import PokemonFactory  # Your custom factory
import sys

pygame.init()

# Create a font for rendering text
FONT = pygame.font.Font(None, 36)

###############################################################################
#                          GIF Loading Utility                                #
###############################################################################
def load_gif(gif_path):
    """Loads a GIF file and returns a list of Pygame surfaces (frames)."""
    frames = []
    gif = Image.open(gif_path)
    for frame_idx in range(gif.n_frames):
        gif.seek(frame_idx)
        frame_image = gif.convert("RGBA")
        frame_surface = pygame.image.fromstring(
            frame_image.tobytes(),
            frame_image.size,
            frame_image.mode
        )
        frames.append(frame_surface)
    return frames

###############################################################################
#                         Drawing the Battle Scene                            #
###############################################################################
def draw_background(screen, location="grassland", time_of_day="day"):
    """Draws the appropriate background and base layer depending on location & time_of_day."""
    if location == "grassland" and time_of_day == "day":
        wallpaper_sprite = "battle sprites/wallpaper/grassland_day.png"
        bases_sprite = "battle sprites/bases/grass_day.png"
    else:
        # Add more conditions for different backgrounds as you wish
        wallpaper_sprite = "battle sprites/wallpaper/grassland_day.png"
        bases_sprite = "battle sprites/bases/grass_day.png"

    # Scale and draw wallpaper
    wallpaper = pygame.transform.scale(
        pygame.image.load(wallpaper_sprite),
        (screen.get_width(), screen.get_height())
    )
    screen.blit(wallpaper, (0, 0))

    # Scale and draw bases (foreground, e.g. grass base platforms)
    bases = pygame.transform.scale(
        pygame.image.load(bases_sprite),
        (screen.get_width(), screen.get_height())
    )
    screen.blit(bases, (0, 0))

def draw_player_pokemon(screen, pokemon, base_x, base_y, frame):
    """Draws the player's Pokémon (using back sprite)."""
    player_frames = load_gif(pokemon.back_sprite)
    player_sprite = player_frames[frame % len(player_frames)]

    # Scale up the sprite (8x as an example)
    original_size = player_sprite.get_size()
    scaled_sprite = pygame.transform.scale(
        player_sprite,
        (original_size[0] * 8, original_size[1] * 8)
    )
    
    # Position so that the bottom of the sprite is at (base_x, base_y)
    sprite_rect = scaled_sprite.get_rect()
    sprite_rect.midbottom = (base_x, base_y)
    screen.blit(scaled_sprite, sprite_rect)

def draw_opponent_pokemon(screen, pokemon, base_x, base_y, frame):
    """Draws the opponent's Pokémon (using front sprite)."""
    opponent_frames = load_gif(pokemon.front_sprite)
    opponent_sprite = opponent_frames[frame % len(opponent_frames)]

    # Scale up the sprite (8x as an example)
    original_size = opponent_sprite.get_size()
    scaled_sprite = pygame.transform.scale(
        opponent_sprite,
        (original_size[0] * 8, original_size[1] * 8)
    )
    
    # Position so that the bottom of the sprite is at (base_x, base_y)
    sprite_rect = scaled_sprite.get_rect()
    sprite_rect.midbottom = (base_x, base_y)
    screen.blit(scaled_sprite, sprite_rect)

def draw_battle(screen, player_pokemon, opponent_pokemon, frame, location="grassland", time_of_day="day"):
    """High-level function to draw the entire battle scene (background + two Pokémon)."""
    draw_background(screen, location, time_of_day)
    
    # Get screen dimensions
    width = screen.get_width()
    height = screen.get_height()
    
    # Example positions
    player_x = int(width * 0.25)
    player_y = int(height * 1.04)   # a bit below the center
    opponent_x = int(width * 0.75)
    opponent_y = int(height * 0.65) # a bit above the center

    # Draw Pokémon
    draw_player_pokemon(screen, player_pokemon, player_x, player_y, frame)
    draw_opponent_pokemon(screen, opponent_pokemon, opponent_x, opponent_y, frame)

###############################################################################
#                            Start Screen Logic                               #
###############################################################################
def start_screen(screen):
    """
    Displays a start screen where the user can type two Pokémon IDs
    and click a "Start Battle" button. Returns (player_id, opponent_id).
    Returns (None, None) if the user quits before starting.
    """
    clock = pygame.time.Clock()

    # Text fields
    player_input = ""
    opponent_input = ""

    # Rectangles for input boxes
    input_box1 = pygame.Rect(100, 100, 140, 32)
    input_box2 = pygame.Rect(100, 150, 140, 32)

    # Button
    button_rect = pygame.Rect(screen.get_width() // 2 - 50, screen.get_height() - 100, 100, 50)
    button_color = (0, 255, 0)

    # Which input box is active?
    active_box = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None, None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    # If the user clicks on the button, return the IDs
                    return player_input, opponent_input
                elif input_box1.collidepoint(event.pos):
                    active_box = 1
                elif input_box2.collidepoint(event.pos):
                    active_box = 2
                else:
                    active_box = None

            elif event.type == pygame.KEYDOWN:
                if active_box == 1:
                    # Editing player_input
                    if event.key == pygame.K_BACKSPACE:
                        player_input = player_input[:-1]
                    else:
                        player_input += event.unicode
                elif active_box == 2:
                    # Editing opponent_input
                    if event.key == pygame.K_BACKSPACE:
                        opponent_input = opponent_input[:-1]
                    else:
                        opponent_input += event.unicode

        # Draw wallpaper in the background
        wallpaper = pygame.transform.scale(
            pygame.image.load("battle sprites/wallpaper/grassland_day.png"),
            (screen.get_width(), screen.get_height())
        )
        screen.blit(wallpaper, (0, 0))

        # Info text at the top
        info_text = FONT.render(
            'Enter two Pokemon IDs (1-151) and click "Start Battle".',
            True, 
            (255, 255, 255)
        )
        screen.blit(info_text, (50, 50))

        # Draw input boxes
        pygame.draw.rect(screen, (255, 255, 255), input_box1, 2)
        pygame.draw.rect(screen, (255, 255, 255), input_box2, 2)

        # Render the text that’s currently in the input boxes
        txt_surface1 = FONT.render(player_input, True, (255, 255, 255))
        txt_surface2 = FONT.render(opponent_input, True, (255, 255, 255))

        screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))

        # Dynamically resize the input box if needed
        input_box1.w = max(200, txt_surface1.get_width() + 10)
        input_box2.w = max(200, txt_surface2.get_width() + 10)

        # Draw "Start Battle" button
        pygame.draw.rect(screen, button_color, button_rect)
        button_text = FONT.render("Start Battle", True, (0, 0, 0))
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

        pygame.display.flip()
        clock.tick(30)  # limit to 30 FPS

###############################################################################
#                                Main Loop                                    #
###############################################################################
def main():
    # Create a resizable screen
    info = pygame.display.Info()
    screen_width, screen_height = info.current_w, info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Pokemon Remake")

    # 1) Start Screen
    player_id, opponent_id = start_screen(screen)
    if player_id is None or opponent_id is None:
        # User quit or something went wrong
        pygame.quit()
        sys.exit()

    # 2) Create Pokémon from user input
    try:
        player_pokemon = PokemonFactory.create_pokemon(int(player_id))
        opponent_pokemon = PokemonFactory.create_pokemon(int(opponent_id))
    except ValueError:
        print("Invalid IDs. Make sure you entered integers.")
        pygame.quit()
        sys.exit()
    except Exception as e:
        print(f"Error creating Pokémon: {e}")
        pygame.quit()
        sys.exit()

    # 3) Battle Loop
    clock = pygame.time.Clock()
    start_time = time.time()
    running = True
    while running:
        frame = int((time.time() - start_time) * 10)  # Adjust speed as needed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the battle scene each frame
        draw_battle(screen, player_pokemon, opponent_pokemon, frame)

        # Flip the display
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
