import random

class battle:
    def __init__(self, player_pokemon, opponent_pokemon) -> None:
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon

    def battle_cry(self):
        print(f"A wild \033[33m{self.opponent_pokemon.name}\033[0m has appeared!")
        print(f"Go! \033[33m{self.player_pokemon.name}\033[0m!")

    def battle_graphic(self):
        print()
        self.opponent_pokemon.identifiers()
        print()
        self.opponent_pokemon.graphics()
        print()
        self.player_pokemon.graphics()
        print()
        self.player_pokemon.identifiers()
        print()

    def battle_logic(self):
        self.battle_cry()
        self.battle_graphic()

        attack_first = self.calculate_attack_first()

    def calculate_attack_first(self):
        if self.player_pokemon.speed > self.opponent_pokemon.speed:
            attack_first = True
        elif self.opponent_pokemon.speed > self.player_pokemon.speed:
            attack_first = False
        else:
            if random.choice([self.player_pokemon.name, self.opponent_pokemon.name]) == self.player_pokemon.name:
                attack_first = True
            else:
                attack_first = False
        return attack_first

    def menu_graphics(self):
        print("0) Fight")
        print("1) Pokemon")
        print("2) Ball")
        print("3) Run")
    
    def menu_logic(self):
        player_input = int(input(f"What will \033[33m{self.player_pokemon.name}\033[0m do? "))
        match player_input:
            case 0:

            case 1:
                pass
            case 2:
                pass
            case 3:
                pass

    def fight_menu_graphics(self):
        self.player_pokemon