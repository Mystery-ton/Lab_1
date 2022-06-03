from animals.Herbivore import Herbivore


class Mouse(Herbivore):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 1
        self.max_age = 25
        self.symbol = "mu"

    def clone(self, name: str) -> "Mouse":
        return super().clone(Mouse(name))
