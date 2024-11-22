import random

class pokemon():

    # constructor
    def __init__(self, name: str, max_health: int, current_health: int):
        self.name = name 
        self.max_health = max_health
        self.current_health = current_health

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
        while health_bars != 0:
            health_bar += "="
            health_bars -=1
        while lost_health_bars != 0:
            health_bar += "-"
            lost_health_bars -= 1
        return print(health_bar)

    # test method
    def __str__(self):
        return f"{self.name}, {self.current_health}"