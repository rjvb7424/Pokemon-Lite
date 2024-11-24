from move_pool import move_pool

class pokemon:
    def __init__(self, name: str, art: str, 
                max_hp: int, current_hp: int, 
                level: int, 
                max_xp: int, current_xp: int,
                attack: int, defence: int, speed: int,
                moves) -> None:
        self.name = name
        self.art = art
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.level = level
        self.max_xp = max_xp
        self.current_xp = current_xp
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.moves = moves

    def calculate_bars(self, bar_max, current_value):
        bar = ""
        BAR_LENGTH = 10
        bar_ratio = bar_max // BAR_LENGTH
        filled_bars = current_value // bar_ratio
        empty_bars = BAR_LENGTH - filled_bars
        bar = "=" * filled_bars + "-" * empty_bars
        return bar
    
    def identifiers(self):
        hp_bar = self.calculate_bars(self.max_hp, self.current_hp)
        xp_bar = self.calculate_bars(self.max_xp, self.current_xp)
        print(f"LVL \033[32m{self.level}\033[0m \033[33m{self.name}\033[0m")
        print(f"HP \033[31m{hp_bar}\033[0m {self.current_hp}/{self.max_hp}")
        print(f"XP \033[32m{xp_bar}\033[0m {self.current_xp}/{self.max_xp}")
    
    def level_check(self):
        if self.current_xp >= self.max_xp:
            while self.current_xp >= self.max_xp:
                self.level += 1
                self.current_xp -= self.max_xp
                self.max_xp = 2 * self.level**2
                self.max_hp = self.max_hp + ((self.level//10) + 4)
                self.current_hp = self.max_hp
                print(f"\033[33m{self.name}\033[0m grew to level \033[32m{self.level}\033[0m!")

    def graphics(self):
        print(self.art)