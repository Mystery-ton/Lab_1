from animals.Omnivorous import Omnivorous


class Chipmunk(Omnivorous):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 2
        self.max_age = 30
        self.symbol = "ch"

    def clone(self, name: str) -> "Chipmunk":
        return super().clone(Chipmunk(name))
