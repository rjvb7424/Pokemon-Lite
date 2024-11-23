import random

class pokemon():

    # constructor
    def __init__(self, name: str, current_health: int, max_health: int, move_ids, speed: int):
        self.name = name 
        self.max_health = max_health
        self.current_health = current_health
        self.moves = self.fetch_moves(move_ids)
        self.speed = speed

    def fetch_moves(self, move_ids):
        
        moves = {}
        move_pool = {
            1: {"name": "bite", "damage": 15},
            2: {"name": "punch", "damage": 10},
            3: {"name": "kick", "damage": 5}}

        added_moves_counter = 0
        for i in move_pool:
            if i in move_ids:
                moves[added_moves_counter] = move_pool[i]
                added_moves_counter += 1
        return moves

    def render_health_bar(self):

        # lets say you have 20 health with a max health bar of 10 bars. 
        # You divide the health by the health bars which gives you how much health one health bar is 'worth'
        # To then update the health bar, for example you sufer 4 points woth of damage so 2 bars, 
        # so you muliply the new heatlh by the health bar ratio

        health_bar = ""
        MAX_HEALTH_BAR = 10
        health_ratio = self.max_health // MAX_HEALTH_BAR
        health_bars = self.current_health // health_ratio
        lost_health_bars = MAX_HEALTH_BAR - health_bars
        while health_bars > 0:
            health_bar += "="
            health_bars -=1
        while lost_health_bars > 0:
            health_bar += "-"
            lost_health_bars -= 1
        return health_bar
    
    def render_identifier(self):

        # function to identify the pokemon, this whill include its name, health and experience

        health_bar = self.render_health_bar()
        return f"{health_bar}, {self.name}"
    
    def battle(self, pokemon_opponent):
        
        # print out identifiers for both the players pokemon along side the opponents pokemon 

        while self.current_health > 0 and pokemon_opponent.current_health > 0:
            print(self.render_identifier())
            print("vs")
            print(pokemon_opponent.render_identifier())

            # print out a list of possible moves for the players pokemon
            # select the player move

            for i in self.moves:
                print(f"{i+1}) name: {self.moves[i]['name']} damage: {self.moves[i]['damage']}", end = "\n")
            player_input = int(input("select move: "))

            # determin who attacks first
            if self.speed > pokemon_opponent.speed:
                attack_first = True
            elif pokemon_opponent.speed > self.speed:
                attack_first = False
            else:
                if random.choice(self.name, pokemon_opponent.name) == self.name:
                    attack_first = True
                else:
                    attack_first = False

            # execute attack order accordingly 

        if self.current_health <= 0:
            print("You have fainted!")
        elif pokemon_opponent.current_health <= 0:
            print("Opponent Pokemon has fainted!")
        else: 
            print("Error")


    # test method
    def __str__(self):
        return f"{self.name}, {self.current_health}"