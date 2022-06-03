from animals.Predator import Predator


class Lynx(Predator):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 2
        self.max_age = 30
        self.symbol = "lx"

    def clone(self, name: str) -> "Lynx":
        return super().clone(Lynx(name))
