from animals.Omnivorous import Omnivorous


class Bear(Omnivorous):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 5
        self.max_age = 45
        self.symbol = "br"

    def clone(self, name: str) -> "Bear":
        return super().clone(Bear(name))
