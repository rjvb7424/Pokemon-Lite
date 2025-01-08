from pokemon import Pokemon
import json

with open("pokemon.json", "r") as file:
    pokemon_data = json.load(file)



class PokemonFactory:
    def __init__(self, id):
        self.id = id


    pokemon = Pokemon(
        id=pokemon_data[id]["id"],
        base_health_points=pokemon_data[id]["base_statistics"]["health_points"],
        base_attack=pokemon_data[id]["base_statistics"]["attack"],
        base_defense=pokemon_data[id]["base_statistics"]["defense"],
        base_special_attack=pokemon_data[id]["base_statistics"]["special_attack"],
        base_special_defense=pokemon_data[id]["base_statistics"]["special_defense"],
        base_speed=pokemon_data[id]["base_statistics"]["speed"],
        name=pokemon_data[id]["name"],
    )