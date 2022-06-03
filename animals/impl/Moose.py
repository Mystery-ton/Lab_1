from animals.Herbivore import Herbivore


class Moose(Herbivore):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 4
        self.max_age = 30
        self.symbol = "mo"

    def clone(self, name: str) -> "Moose":
        return super().clone(Moose(name))
