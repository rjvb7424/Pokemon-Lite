# battle.py

import tkinter as tk
from PIL import Image, ImageTk
import pygame

def load_gif_frames(filepath):
    """
    Loads all frames from a GIF file and returns them as a list of PIL Images.
    """
    frames = []
    pil_image = Image.open(filepath)

    try:
        while True:
            frames.append(pil_image.copy())
            pil_image.seek(len(frames))  # Move to the next frame
    except EOFError:
        pass  # No more frames

    return frames

def upscale_frames(frames, scale_factor):
    """
    Upscales each frame by `scale_factor` using NEAREST interpolation 
    to preserve the pixelated look.
    Returns a list of Tkinter PhotoImage objects.
    """
    upscaled = []
    for frame in frames:
        w, h = frame.size
        resized = frame.resize((w * scale_factor, h * scale_factor), Image.NEAREST)
        upscaled.append(ImageTk.PhotoImage(resized))
    return upscaled

def animate_frames(root, label, frames, delay=100, index=0):
    """
    Recursively updates the 'label' with the next frame in 'frames' every 'delay' ms.
    """
    if not frames:
        return

    # Display the current frame
    label.config(image=frames[index])

    # Schedule the next frame
    next_index = (index + 1) % len(frames)
    root.after(delay, animate_frames, root, label, frames, delay, next_index)

def start_battle(player_pokemon, opponent_pokemon, 
                 player_scale=8, opponent_scale=8, 
                 frame_delay=100, 
                 window_title="Pokémon Battle"):
    """
    Creates a new window showing a simple battle scene:
    - Player Pokémon (back sprite) at bottom-left
    - Opponent Pokémon (front sprite) at top-right
    - Plays each Pokémon's cry if available.
    """

    # 1. Initialize Pygame mixer for sound
    pygame.mixer.init()

    # 2. Create the main battle window
    root = tk.Tk()
    root.title(window_title)
    root.configure(bg="black")

    # Optional: set a fixed window size or just let Tk compute
    # root.geometry("800x600")  # Example for a fixed size

    # 3. Load and upscale frames for player (back sprite)
    if player_pokemon.back_sprite:
        player_frames_pil = load_gif_frames(player_pokemon.back_sprite)
        player_frames_upscaled = upscale_frames(player_frames_pil, player_scale)
    else:
        player_frames_upscaled = []

    # 4. Load and upscale frames for opponent (front sprite)
    if opponent_pokemon.front_sprite:
        opponent_frames_pil = load_gif_frames(opponent_pokemon.front_sprite)
        opponent_frames_upscaled = upscale_frames(opponent_frames_pil, opponent_scale)
    else:
        opponent_frames_upscaled = []

    # 5. Create labels for both sprites
    #    We'll use place() for absolute positioning to emulate a classic Pokémon layout.
    player_label = tk.Label(root, bg="black")
    opponent_label = tk.Label(root, bg="black")

    player_label.place(x=50, rely=0.8, anchor='sw')      # bottom-left region
    opponent_label.place(relx=0.95, y=50, anchor='ne')   # top-right region

    # 6. Animate the sprites
    #    We can animate both if they have frames
    if player_frames_upscaled:
        animate_frames(root, player_label, player_frames_upscaled, delay=frame_delay)

    if opponent_frames_upscaled:
        animate_frames(root, opponent_label, opponent_frames_upscaled, delay=frame_delay)

    # 7. Play the Pokémon cries if available
    if player_pokemon.cry:
        player_cry_sound = pygame.mixer.Sound(player_pokemon.cry)
        player_cry_sound.play()
    if opponent_pokemon.cry:
        opponent_cry_sound = pygame.mixer.Sound(opponent_pokemon.cry)
        opponent_cry_sound.play()

    # 8. Start the main loop
    root.mainloop()
