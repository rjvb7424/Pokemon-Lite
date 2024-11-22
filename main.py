from pokemon import pokemon

pokemon1 = pokemon("Pikachu", 20, 20)

print(pokemon1)
pokemon1.render_health_bar()
pokemon1.current_health = 2
pokemon1.render_health_bar()