from Animal import Animal


class Herbivore(Animal):
    __INITIAL_HUNGER_AMOUNT_OF_HERBIVORE: int = 8

    def __init__(self,type,food_priority,max_age,symbol):
        super().__init__()
        self.is_predator = False
        self.hunger = self.__INITIAL_HUNGER_AMOUNT_OF_HERBIVORE
        self.type = type
        self.food_priority = food_priority
        self.max_age = max_age
        self.symbol = symbol

    def clone(self, type: str, food_priority:int, max_age:int, symbol:str) -> "Animal":
        return super().clone(Herbivore(type,food_priority,max_age, symbol))