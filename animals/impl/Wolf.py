from animals.Predator import Predator


class Wolf(Predator):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 4
        self.max_age = 40
        self.symbol = "wo"

    def clone(self, name: str) -> "Wolf":
        return super().clone(Wolf(name))
