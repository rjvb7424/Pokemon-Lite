import tkinter as tk
from PIL import Image, ImageTk
import pygame


def load_gif_frames(filepath):
    """
    Loads all frames from a GIF file and returns them as a list of PIL images.
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


def center_window(root, widget):
    """
    Centers the main Tkinter window on the screen based on the
    size requested by 'widget'.
    """
    # Let Tkinter compute the geometry
    root.update_idletasks()

    # Dimensions of the widget
    window_width = widget.winfo_reqwidth()
    window_height = widget.winfo_reqheight()

    # Dimensions of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the geometry
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")


def display_pokemon(pokemon, scale_factor=8, frame_delay=100):
    """
    Displays the Pokemon's sprite (GIF) in a Tkinter window (centered) 
    and plays the Pokemon's cry using pygame.
    """
    # Initialize pygame mixer for sound
    pygame.mixer.init()

    # Create main window
    root = tk.Tk()
    root.title(f"{pokemon.name} Display")
    root.configure(bg="black")

    # 1. Load frames from sprite
    frames_pil = load_gif_frames(pokemon.front_sprite)

    # 2. Upscale frames
    upscaled_frames = upscale_frames(frames_pil, scale_factor)

    # 3. Create a label to display the frames
    sprite_label = tk.Label(root, bg="black")
    sprite_label.pack(expand=True)

    # 4. Animate frames
    animate_frames(root, sprite_label, upscaled_frames, delay=frame_delay)

    # 5. Play sound
    if pokemon.cry:
        cry_sound = pygame.mixer.Sound(pokemon.cry)
        cry_sound.play()

    # 6. Center the window
    center_window(root, sprite_label)

    # 7. Start the main event loop
    root.mainloop()
