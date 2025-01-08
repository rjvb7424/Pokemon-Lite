from pokemon import Pokemon
import

class PokemonFactory:
    def __init__(self, id):
        self.id = id
        api_url = "https://pokeapi.co/api/v2/pokemon"
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
    pokemon = Pokemon()