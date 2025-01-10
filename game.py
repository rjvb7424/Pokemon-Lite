import pygame
import time
import sys
from PIL import Image
from pokemon_factory import PokemonFactory  # Your custom factory

pygame.init()
pygame.mixer.init()  # Ensure the sound mixer is initialized
FONT = pygame.font.Font(None, 36)

###############################################################################
#                         GIF Loading Utility                                 #
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
#                          Drawing the Battle Scene                           #
###############################################################################
def draw_background(screen, location="grassland", time_of_day="day"):
    """Draws the appropriate background and base layer depending on location & time_of_day."""
    if location == "grassland" and time_of_day == "day":
        wallpaper_sprite = "battle sprites/wallpaper/grassland_day.png"
        bases_sprite = "battle sprites/bases/grass_day.png"
    else:
        # Fallback or other backgrounds here
        wallpaper_sprite = "battle sprites/wallpaper/grassland_day.png"
        bases_sprite = "battle sprites/bases/grass_day.png"

    # Scale and draw wallpaper
    wallpaper = pygame.transform.scale(
        pygame.image.load(wallpaper_sprite),
        (screen.get_width(), screen.get_height())
    )
    screen.blit(wallpaper, (0, 0))

    # Scale and draw bases
    bases = pygame.transform.scale(
        pygame.image.load(bases_sprite),
        (screen.get_width(), screen.get_height())
    )
    screen.blit(bases, (0, 0))

def draw_player_pokemon(screen, pokemon, base_x, base_y, frame):
    """Draws the player's Pokémon using its back sprite."""
    frames = load_gif(pokemon.back_sprite)
    sprite = frames[frame % len(frames)]

    # Scale up the sprite (8x is just an example)
    original_size = sprite.get_size()
    scaled_sprite = pygame.transform.scale(sprite, (original_size[0]*8, original_size[1]*8))
    
    # Position so that the bottom of the sprite is at (base_x, base_y)
    sprite_rect = scaled_sprite.get_rect()
    sprite_rect.midbottom = (base_x, base_y)
    screen.blit(scaled_sprite, sprite_rect)

def draw_opponent_pokemon(screen, pokemon, base_x, base_y, frame):
    """Draws the opponent's Pokémon using its front sprite."""
    frames = load_gif(pokemon.front_sprite)
    sprite = frames[frame % len(frames)]

    # Scale up the sprite
    original_size = sprite.get_size()
    scaled_sprite = pygame.transform.scale(sprite, (original_size[0]*8, original_size[1]*8))
    
    # Position so that the bottom of the sprite is at (base_x, base_y)
    sprite_rect = scaled_sprite.get_rect()
    sprite_rect.midbottom = (base_x, base_y)
    screen.blit(scaled_sprite, sprite_rect)

def draw_battle(screen, player_pokemon, opponent_pokemon, frame):
    """High-level function to draw the entire battle scene (background + Pokémon)."""
    draw_background(screen, location="grassland", time_of_day="day")
    
    # Determine positions
    width, height = screen.get_width(), screen.get_height()
    
    player_x = int(width * 0.25)
    player_y = int(height * 1.04)   # tweak as needed
    opponent_x = int(width * 0.75)
    opponent_y = int(height * 0.65)

    draw_player_pokemon(screen, player_pokemon, player_x, player_y, frame)
    draw_opponent_pokemon(screen, opponent_pokemon, opponent_x, opponent_y, frame)

###############################################################################
#                           Start Screen Function                             #
###############################################################################
def start_screen(screen):
    """
    Displays a start screen where the user can type two Pokémon IDs
    and click a "Start Battle" button.
    Returns (player_id, opponent_id) when the user clicks the button.
    Returns (None, None) if the user quits.
    """
    clock = pygame.time.Clock()

    # Text fields
    player_input = ""
    opponent_input = ""

    # Rectangles for input boxes
    input_box1 = pygame.Rect(100, 100, 140, 32)
    input_box2 = pygame.Rect(100, 150, 140, 32)

    # Button
    button_rect = pygame.Rect(screen.get_width()//2 - 50, screen.get_height() - 100, 100, 50)
    button_color = (0, 255, 0)

    # Which input box is active?
    active_box = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None, None  # user closed the game

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    # User clicked the "Start Battle" button
                    return player_input, opponent_input
                elif input_box1.collidepoint(event.pos):
                    active_box = 1
                elif input_box2.collidepoint(event.pos):
                    active_box = 2
                else:
                    active_box = None

            elif event.type == pygame.KEYDOWN:
                if active_box == 1:
                    if event.key == pygame.K_BACKSPACE:
                        player_input = player_input[:-1]
                    else:
                        player_input += event.unicode
                elif active_box == 2:
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

        # Info text
        info_text = FONT.render(
            'Enter two Pokemon IDs (1-151) and click "Start Battle".',
            True,
            (255, 255, 255)
        )
        screen.blit(info_text, (50, 50))

        # Draw input boxes
        pygame.draw.rect(screen, (255, 255, 255), input_box1, 2)
        pygame.draw.rect(screen, (255, 255, 255), input_box2, 2)

        # Render current text in the input boxes
        txt_surface1 = FONT.render(player_input, True, (255, 255, 255))
        txt_surface2 = FONT.render(opponent_input, True, (255, 255, 255))
        screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))

        # Dynamically resize input boxes
        input_box1.w = max(200, txt_surface1.get_width() + 10)
        input_box2.w = max(200, txt_surface2.get_width() + 10)

        # Draw "Start Battle" button
        pygame.draw.rect(screen, button_color, button_rect)
        button_text = FONT.render("Start Battle", True, (0, 0, 0))
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

        pygame.display.flip()
        clock.tick(30)

###############################################################################
#                          Battle Screen Function                              #
###############################################################################
def battle_screen(screen, player_pokemon, opponent_pokemon):
    """
    Displays the battle scene (with animations) and includes a 'Back' button
    for returning to the start screen. Also plays the player's cry first,
    then opponent's cry after 1.5 seconds.
    
    Returns True if user clicked 'Back', or False if user closed the window.
    """
    clock = pygame.time.Clock()
    start_time = time.time()

    # "Back" button
    back_button_rect = pygame.Rect(10, 10, 80, 40)
    back_button_color = (255, 0, 0)

    # Load the cry sounds
    try:
        player_cry = pygame.mixer.Sound(player_pokemon.cry)
        opponent_cry = pygame.mixer.Sound(opponent_pokemon.cry)
    except Exception as e:
        print("Error loading cry sound:", e)
        player_cry, opponent_cry = None, None

    # Flags for playing cries
    player_cry_played = False
    opponent_cry_played = False
    time_for_opponent_cry = 0

    running = True
    while running:
        frame = int((time.time() - start_time) * 10)  # animate speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # user closed the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    # User clicked the Back button
                    return True

        # Play the player's cry once, then queue the opponent's cry
        if not player_cry_played and player_cry:
            player_cry.play()
            player_cry_played = True
            # Schedule opponent's cry in 1.5 seconds
            time_for_opponent_cry = time.time() + 1.5

        # Once 1.5 seconds have passed, play opponent's cry
        if player_cry_played and not opponent_cry_played and opponent_cry:
            if time.time() >= time_for_opponent_cry:
                opponent_cry.play()
                opponent_cry_played = True

        # Draw battle background + Pokémon
        draw_battle(screen, player_pokemon, opponent_pokemon, frame)

        # Draw "Back" button
        pygame.draw.rect(screen, back_button_color, back_button_rect)
        back_text = FONT.render("Back", True, (255, 255, 255))
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, back_text_rect)

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    return False

###############################################################################
#                                Main                                         #
###############################################################################
def main():
    info = pygame.display.Info()
    screen_width, screen_height = info.current_w, info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Pokemon Lite")

    while True:
        # 1) Show the Start Screen
        player_id, opponent_id = start_screen(screen)
        if player_id is None or opponent_id is None:
            # User closed the game on the start screen
            pygame.quit()
            sys.exit()

        # 2) Create the Pokémon objects from user input
        try:
            p_id = int(player_id)
            o_id = int(opponent_id)
            player_pokemon = PokemonFactory.create_pokemon(p_id)
            opponent_pokemon = PokemonFactory.create_pokemon(o_id)
        except Exception as e:
            print(f"Error creating Pokémon: {e}")
            pygame.quit()
            sys.exit()

        # 3) Go to the Battle Screen
        go_back = battle_screen(screen, player_pokemon, opponent_pokemon)

        if not go_back:
            # User closed the game window on the battle screen
            pygame.quit()
            sys.exit()
        # Otherwise, user clicked 'Back', so loop again -> show start screen

if __name__ == "__main__":
    main()
