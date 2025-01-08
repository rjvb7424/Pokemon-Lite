from battle_view import setup_battle_screen
from pokemon_factory import PokemonFactory

player_pokemon = PokemonFactory.create_pokemon(25)
opponent_pokemon = PokemonFactory.create_pokemon(26)

setup_battle_screen(player_pokemon, opponent_pokemon, "battle sprites/wallpaper/grassland_day.png", "battle sprites/bases/grass_day.png")