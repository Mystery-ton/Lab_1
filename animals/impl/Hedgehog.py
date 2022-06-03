from animals.Omnivorous import Omnivorous


class Hedgehog(Omnivorous):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.food_priority = 2
        self.max_age = 125
        self.symbol = "hd"

    def clone(self, name: str) -> "Hedgehog":
        return super().clone(Hedgehog(name))
