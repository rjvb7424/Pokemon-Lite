from pokemon import pokemon

pokemon1 = pokemon("Pikachu", 10, 10, [3, 1])
pokemon_opponent = pokemon("Eve", 10, 10, [2, 1])

pokemon1.battle(pokemon_opponent)