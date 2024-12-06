from pokemon import pokemon

class move:
    def __init__(self, name: str, power: int, accuracy: int, type_: str, max_pp: int = 10):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.type_ = type_
        self.max_pp = max_pp
        self.pp = max_pp

    def __repr__(self):
        return f"Move({self.name}, Power: {self.power}, Accuracy: {self.accuracy}, Type: {self.type_}, PP: {self.pp}/{self.max_pp})"

class moves:
    def __init__(self):
        self.move_list = []

    def append(self, move):
        self.move_list.append(move)

    def __getitem__(self, index):
        return self.move_list[index]

    def __len__(self):
        return len(self.move_list)

    def __repr__(self):
        return f"Moves: {[move.name for move in self.move_list]}"
