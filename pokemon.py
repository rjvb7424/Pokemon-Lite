import random

class Pokemon:
    def __init__(self, index, 
                base_health_points, base_attack, base_defense, base_special_attack, base_special_defense, base_speed):

        # Cries, front and back sprites have been stored in a way in which the name of the file corespondes to the index of that pokemon. 
        self.index = index
        self.cry = f"cries/{index}.ogg"
        self.front_sprite = f"pokemon sprites/front/{index}.gif"
        self.back_sprite = f"pokemon sprites/back/{index}.gif"

        # The base statistics of the pokemon will be stored in a dictionary.
        self.base_statistics = {
            "health points": base_health_points,
            "attack": base_attack,
            "defense": base_defense,
            "special attack": base_special_attack,
            "special defense": base_special_defense,
            "speed": base_speed,
            }
        
        # Individual Values (IV) represent a Pokemon's genetic potential for each statistic. 
        # They are randomly generated from a range of 0 to 31. 
        # This results in the same Pokemon with a health IV of 31 ending up with more health.
        self.individual_values = {
            "health points": random.randrange(0, 32),
            "attack": random.randrange(0, 32),
            "defense": random.randrange(0, 32),
            "special attack": random.randrange(0, 32),
            "special defense": random.randrange(0, 32),
            "speed": random.randrange(0, 32),
        }

        # Effort Values (EV) are gained through battling other Pokemon. 
        # In a range of 0 to 252 per statistic. 
        # They are gained from battling Pokemon's that yield a certain EV.
        self.effort_values = {
            "health points": 0,
            "attack": 0,
            "defense": 0,
            "special attack": 0,
            "special defense": 0,
            "speed": 0,
        }

        # The statistics of the pokemon will be stored in a dictionary. 
        # The statistics are calculated using the formula
        # dwdad in the calculate_hp_stat
        self.statistics = {
            "health points": self.calculate_hp_stat(self.base_statistics["health points"], 
                                                    self.individual_values["health points"], 
                                                    self.effort_values["health points"], 
                                                    self.level),
        }

    def calculate_health_points_statistic(base_statistic, individual_values, effort_values, level):
        return int((((base_statistic * 2) + individual_values + (effort_values / 4)) * (level / 100)) + level + 10)
    
    def calculate_other_statistics(base_statistic, individual_values, effort_values, level, nature_multiplier=1.0):
        stat = int((((base_stat * 2) + iv + (ev / 4)) * (level / 100)) + 5)
        return int(stat * nature_multiplier)