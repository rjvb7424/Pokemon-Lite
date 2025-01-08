import requests
import json
import time

id_max = 9

with open("pokemon.json", "w") as file:

    for id in range(1, id_max + 1):

        # Sets up the API request.
        api_url = "https://pokeapi.co/api/v2/pokemon"
        response = requests.get(f"{api_url}/{id}").json()

        # Extract the base statistics from the PokeAPI.
        health_points = response["stats"][0]["base_stat"]
        attack = response["stats"][1]["base_stat"]
        defense = response["stats"][2]["base_stat"]
        special_attack = response["stats"][3]["base_stat"]
        special_defense = response["stats"][4]["base_stat"]
        speed = response["stats"][5]["base_stat"]

        # Extracts some usefull information about the Pokemon.
        name = response["name"]
        base_experience = response["base_experience"]
        first_type = response["types"][0]["type"]["name"]
        # If the Pokemon has two types, extract the second type.
        second_type = response["types"][1]["type"]["name"] if len(response["types"]) == 2 else None

        # Create a dictionary to store the Pokemon's information.
        pokemon = {
            "name": name,
            "base statistics": {
                "health points": health_points,
                "attack": attack,
                "defense": defense,
                "special attack": special_attack,
                "special defense": special_defense,
                "speed": speed,
            },
            "base_experience": base_experience,
            "types": (first_type, second_type),
        }

        file.write(json.dumps(pokemon, indent=4))
        print(f"Pokemon {name} written to file. {id//id_max*100}%")
        time.sleep(1)