import requests
import json
import time

# The maximum ID of the Pokémon to fetch from the API.
id_max = 20
# A list to store all Pokémon data.
# This is done to avoid writing to the file every time a Pokémon is fetched.
pokemon_list = []

# For loop will run from 1, as the first Pokémon has an ID of 1.
# 1 is being added because the range function is up to but not including the second argument.
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

    # Extracts some useful information about the Pokémon.
    name = response["name"]
    base_experience = response["base_experience"]
    first_type = response["types"][0]["type"]["name"]
    # If the Pokémon has two types, extract the second type.
    second_type = response["types"][1]["type"]["name"] if len(response["types"]) == 2 else None

    # Create a dictionary to store the Pokémon's information.
    pokemon = {
        "name": name,
        "base_statistics": {
            "health_points": health_points,
            "attack": attack,
            "defense": defense,
            "special_attack": special_attack,
            "special_defense": special_defense,
            "speed": speed,
        },
        "base_experience": base_experience,
        "types": [first_type, second_type] if second_type else [first_type],
    }

    # Append the Pokémon data to the list.
    pokemon_list.append(pokemon)
    print(f"Pokemon {name} added. {id//id_max*100}% completed.")
    time.sleep(1)

# Write all Pokémon data to the JSON file in one go. 
# This is more efficient than writing to the file every time a Pokémon is fetched.
# More over the array is an array of dictionaries, so it can be written to the file in one go.
with open("pokemon.json", "w") as file:
    json.dump(pokemon_list, file, indent=4)