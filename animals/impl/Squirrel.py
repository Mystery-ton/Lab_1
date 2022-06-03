from animals.Herbivore import Herbivore


class Squirrel(Herbivore):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 2
        self.max_age = 25
        self.symbol = "sq"

    def clone(self, name: str) -> "Squirrel":
        return super().clone(Squirrel(name))
