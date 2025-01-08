from pokemon import Pokemon
import json

# Load the Pokemon data from the JSON file.
with open("pokemon.json", "r") as file:
    pokemon_data = json.load(file)

# The PokemonFactory class is responsible for creating Pokemon objects.
# It is a Factory Method, logically this is needed as the Pokemon class is not responsible for creating Pokemon objects. 
# The Pokemon class just provides a template for them.
class PokemonFactory:
    @staticmethod
    def create_pokemon(id):
        return Pokemon(
            id=id,
            base_health_points=pokemon_data[id]["base_statistics"]["health_points"],
            base_attack=pokemon_data[id]["base_statistics"]["attack"],
            base_defense=pokemon_data[id]["base_statistics"]["defense"],
            base_special_attack=pokemon_data[id]["base_statistics"]["special_attack"],
            base_special_defense=pokemon_data[id]["base_statistics"]["special_defense"],
            base_speed=pokemon_data[id]["base_statistics"]["speed"],
            name=pokemon_data[id]["name"],
        )
