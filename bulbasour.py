from pokemon import pokemon

class bulbasour(pokemon):
    def __init__(self, name = "bulbasour", 
                art = "\033[32m o_o\n(\\_/)\n^^ ^^",
                max_hp = 20, current_hp = 20, 
                level = 5, 
                max_xp = 20, current_xp = 0) -> None:
        super().__init__(name, art,  max_hp, current_hp, level, max_xp, current_xp)