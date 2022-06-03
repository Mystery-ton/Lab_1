from animals.Herbivore import Herbivore


class Hare(Herbivore):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 2
        self.max_age = 25
        self.symbol = "ha"

    def clone(self, name: str) -> "Hare":
        return super().clone(Hare(name))
