from pokemon_factory import PokemonFactory
from pokemon_display import display_pokemon

def main():
    pokemon = PokemonFactory.create_pokemon(6)
    
    # Display the Pokemon with default scale (8) and animation delay (100 ms)
    display_pokemon(pokemon)

if __name__ == "__main__":
    main()
