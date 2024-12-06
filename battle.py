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

    def fight_menu_graphics(self):
        print("\033[35mFight Menu:\033[0m")
        for i, move in enumerate(self.player_pokemon.moves):
            print(f"{i}) {move.name} (Power: {move.power}, PP: {move.pp}/{move.max_pp})")

    def fight_menu_logic(self):
        self.fight_menu_graphics()
        while True:
            try:
                player_move_choice = int(input(f"Choose a move for \033[33m{self.player_pokemon.name}\033[0m: "))
                if 0 <= player_move_choice < len(self.player_pokemon.moves):
                    chosen_move = self.player_pokemon.moves[player_move_choice]
                    if chosen_move.pp > 0:
                        return chosen_move
                    else:
                        print("That move has no PP left! Choose another.")
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number corresponding to a move.")

    def battle_logic(self):
        self.battle_cry()
        self.battle_graphic()

        attack_first = self.calculate_attack_first()

        while self.player_pokemon.current_hp > 0 and self.opponent_pokemon.current_hp > 0:
            if attack_first:
                # Player's turn
                chosen_move = self.fight_menu_logic()
                self.use_move(self.player_pokemon, self.opponent_pokemon, chosen_move)
                if self.opponent_pokemon.current_hp <= 0:
                    print(f"\033[33m{self.opponent_pokemon.name}\033[0m fainted!")
                    break

                # Opponent's turn
                opponent_move = random.choice(self.opponent_pokemon.moves)
                self.use_move(self.opponent_pokemon, self.player_pokemon, opponent_move)
                if self.player_pokemon.current_hp <= 0:
                    print(f"\033[33m{self.player_pokemon.name}\033[0m fainted!")
                    break
            else:
                # Opponent's turn
                opponent_move = random.choice(self.opponent_pokemon.moves)
                self.use_move(self.opponent_pokemon, self.player_pokemon, opponent_move)
                if self.player_pokemon.current_hp <= 0:
                    print(f"\033[33m{self.player_pokemon.name}\033[0m fainted!")
                    break

                # Player's turn
                chosen_move = self.fight_menu_logic()
                self.use_move(self.player_pokemon, self.opponent_pokemon, chosen_move)
                if self.opponent_pokemon.current_hp <= 0:
                    print(f"\033[33m{self.opponent_pokemon.name}\033[0m fainted!")
                    break

    def use_move(self, attacker, defender, move):
        if move.pp > 0:
            move.pp -= 1
            damage = max(1, move.power + attacker.attack - defender.defence)
            defender.current_hp = max(0, defender.current_hp - damage)
            print(f"\033[33m{attacker.name}\033[0m used \033[36m{move.name}\033[0m!")
            print(f"It dealt \033[31m{damage}\033[0m damage.")
        else:
            print(f"\033[33m{attacker.name}\033[0m tried to use \033[36m{move.name}\033[0m, but it failed due to no PP left!")
