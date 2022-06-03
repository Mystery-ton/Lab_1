from animals.Herbivore import Herbivore


class Beaver(Herbivore):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 3
        self.max_age = 30
        self.symbol = "bv"

    def clone(self, name: str) -> "Beaver":
        return super().clone(Beaver(name))
