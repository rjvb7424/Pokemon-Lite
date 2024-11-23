from pokemon import pokemon

pokemon1 = pokemon("Pikachu", 30, 30, [3, 1], 10)
pokemon_opponent = pokemon("Eve", 30, 30, [2, 1], 10)

print()
pokemon1.battle(pokemon_opponent)