from pokemon_factory import PokemonFactory
from pokemon_display import display_pokemon
from battle import start_battle

def main():
    player_pokemon = PokemonFactory.create_pokemon(18)
    opponent_pokemon = PokemonFactory.create_pokemon(2)
    
    start_battle(player_pokemon, opponent_pokemon, player_scale=8, opponent_scale=8, frame_delay=100, window_title="Pokémon Battle")

if __name__ == "__main__":
    main()
