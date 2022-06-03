from animals.Predator import Predator


class Fox(Predator):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 3
        self.max_age = 35
        self.symbol = "fo"

    def clone(self, name: str) -> "Fox":
        return super().clone(Fox(name))
