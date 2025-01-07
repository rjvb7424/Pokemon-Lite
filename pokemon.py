class pokemon:
    def __init__(self, index, 
                health_points, attack, defense, special_attack, special_defense, speed):
        
        # Cries, front and back sprites have been stored in a way in which the name of the file corespondes to the index of that pokemon. 
        self.index = index
        self.cry = f"cries/{index}.ogg"
        self.front_sprite = f"sprites/front/{index}.gif"
        self.back_sprite = f"sprites/back/{index}.gif"

        # The statistics of the pokemon will be stored in a dictionary.
        self.statistics = {
            "health points": health_points,
            "attack": attack,
            "defense": defense,
            "special attack": special_attack,
            "special defense": special_defense,
            "speed": speed,
            }