from pokemon import pokemon

class squirtle(pokemon):
    def __init__(self, name = "Squirtle", 
                art = "\033[34m ^_^\n(o.o)\n(__)__\033[0m",
                max_hp = 20, current_hp = 20, 
                level = 5, 
                max_xp = 20, current_xp = 0) -> None:
        super().__init__(name, art,  max_hp, current_hp, level, max_xp, current_xp)