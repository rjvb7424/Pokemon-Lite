import tkinter as tk
from PIL import Image, ImageTk
import pygame
import time

def display_sprite_and_play_sound(pokemon):
    # Initialize pygame mixer for playing the sound
    pygame.mixer.init()

    root = tk.Tk()
    root.title(f"{pokemon.name} Display")

    # --- Load GIF frames using Pillow ---
    # This part reads every frame in the GIF and converts each frame into a PhotoImage.
    pil_image = Image.open(pokemon.front_sprite)
    frames = []
    
    try:
        while True:
            frame = ImageTk.PhotoImage(pil_image.copy())
            frames.append(frame)
            pil_image.seek(len(frames))  # Go to the next frame
    except EOFError:
        pass  # We have reached the end of the GIF

    # Create a Label to display the frames
    label = tk.Label(root)
    label.pack()

    # --- Define a function to loop through the GIF frames ---
    def update_frame(frame_index=0):
        frame = frames[frame_index]
        label.configure(image=frame)
        # Schedule next frame update
        root.after(100, update_frame, (frame_index + 1) % len(frames))

    # Begin animating the GIF
    update_frame()

    # --- Play the sound ---
    cry_sound = pygame.mixer.Sound(pokemon.cry)
    cry_sound.play()

    # Start the Tkinter main event loop
    root.mainloop()


# Example usage:
if __name__ == "__main__":
    import requests
    from pokemon import Pokemon
    
    index = 3
    url = "https://pokeapi.co/api/v2/pokemon"
    response = requests.get(f"{url}/{index}").json()

    health_points = response["stats"][0]["base_stat"]
    attack = response["stats"][1]["base_stat"]
    defense = response["stats"][2]["base_stat"]
    special_attack = response["stats"][3]["base_stat"]
    special_defense = response["stats"][4]["base_stat"]
    speed = response["stats"][5]["base_stat"]
    name = response["name"]

    # Instantiate your Pokemon object
    pokemon = Pokemon(index,
                      health_points, 
                      attack, 
                      defense, 
                      special_attack, 
                      special_defense, 
                      speed, 
                      name, 
                      level=50)

    # Display sprite and play sound
    display_sprite_and_play_sound(pokemon)
