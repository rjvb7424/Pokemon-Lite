import tkinter as tk
from PIL import Image, ImageTk
import pygame

def display_sprite_and_play_sound(pokemon):
    # Initialize pygame mixer for playing the sound
    pygame.mixer.init()

    root = tk.Tk()
    root.title(f"{pokemon.name} Display")
    root.configure(bg="black")  # optional, for contrast around the sprite

    # ==============
    #  LOAD SPRITE
    # ==============
    pil_image = Image.open(pokemon.front_sprite)
    
    # We’re going to extract all frames from the GIF
    frames_pil = []
    try:
        while True:
            frames_pil.append(pil_image.copy())
            pil_image.seek(len(frames_pil))  # move to the next frame
    except EOFError:
        pass  # we’ve reached the end of the GIF

    # ==============
    #  UPSCALE
    # ==============
    # Increase pixel size by a factor (e.g., 4 = 4x bigger)
    scale_factor = 8

    # For each frame, resize it using NEAREST so it remains "pixelated"
    upscaled_frames = []
    for frame_pil in frames_pil:
        w, h = frame_pil.size
        # Resize image to (width * scale_factor, height * scale_factor)
        upscaled_frame = frame_pil.resize((w * scale_factor, h * scale_factor), Image.NEAREST)
        # Convert to a Tkinter-compatible image
        upscaled_frames.append(ImageTk.PhotoImage(upscaled_frame))

    # Create a Label to display the frames
    label = tk.Label(root, bg="black")
    label.pack(expand=True)

    # ==============
    #  ANIMATE GIF
    # ==============
    def update_frame(frame_index=0):
        label.configure(image=upscaled_frames[frame_index])
        # Schedule next frame update (you can tweak 100 ms for speed)
        root.after(100, update_frame, (frame_index + 1) % len(upscaled_frames))

    update_frame()

    # ==============
    #  PLAY SOUND
    # ==============
    cry_sound = pygame.mixer.Sound(pokemon.cry)
    cry_sound.play()

    # ==============
    #  CENTER WINDOW
    # ==============
    # 1. Let Tkinter calculate the size it needs
    root.update_idletasks()
    
    # 2. Get the desired width/height of our image display area
    window_width = label.winfo_reqwidth()
    window_height = label.winfo_reqheight()
    
    # 3. Get the screen's width/height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # 4. Compute x, y coordinates to place window in the center
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    
    # 5. Position the window at (x, y)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Start the Tkinter main event loop
    root.mainloop()


# Example usage:
if __name__ == "__main__":
    import requests
    from pokemon import Pokemon
    


    # Display sprite and play sound (resized and centered)
    display_sprite_and_play_sound(pokemon)
