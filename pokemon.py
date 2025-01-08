import random

class Pokemon:
    def __init__(self, id, 
                base_health_points, base_attack, base_defense, base_special_attack, base_special_defense, base_speed,
                name, level=5):

        # Cries, front and back sprites have been stored in a way in which the name of the file corespondes to the index of that pokemon. 
        self.id = id
        self.cry = f"cries/{id}.ogg"
        self.front_sprite = f"pokemon sprites/front/{id}.gif"
        self.back_sprite = f"pokemon sprites/back/{id}.gif"

        # The nickname of the pokemon will equal to the name, then a setter will be used to change the nickname.
        self.name = name
        self.nickname = name
        self. level = level

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
        # The statistics are calculated using the formula provided by Bulbapedia.
        self.statistics = {
            "health points": self.calculate_health_points_statistic(
                self.base_statistics["health points"], 
                self.individual_values["health points"], 
                self.effort_values["health points"], 
                self.level,),
            "attack": self.calculate_other_statistics(self.base_statistics["attack"],
                self.individual_values["attack"],
                self.effort_values["attack"],
                self.level,),
            "defense": self.calculate_other_statistics(
                self.base_statistics["defense"],
                self.individual_values["defense"],
                self.effort_values["defense"],
                self.level,),
            "special attack": self.calculate_other_statistics(
                self.base_statistics["special attack"],
                self.individual_values["special attack"],
                self.effort_values["special attack"],
                self.level,),
            "special defense": self.calculate_other_statistics(
                self.base_statistics["special defense"],
                self.individual_values["special defense"],
                self.effort_values["special defense"],
                self.level,),
            "speed": self.calculate_other_statistics(
                self.base_statistics["speed"],
                self.individual_values["speed"],
                self.effort_values["speed"],
                self.level,)
        }

    def calculate_health_points_statistic(self, base_statistic, individual_values, effort_values, level):
        statistic = int(((2 * base_statistic + individual_values + (effort_values / 4)) * level) / 100 + level + 10)
        return int(statistic)
    
    # TO DO - Implement natures 
    def calculate_other_statistics(self, base_statistic, individual_values, effort_values, level, nature_multiplier=1.0):
        statistic = int((((2 * base_statistic + individual_values + (effort_values / 4)) * level) / 100 + 5) * nature_multiplier)
        return int(statistic)