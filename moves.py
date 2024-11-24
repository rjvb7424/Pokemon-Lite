class move:
    def __init__(self, name: str, power: int, accuracy: int, type) -> None:
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.type = type

class moves(move): 
    def __init__(self) -> None:
        self.moves = []