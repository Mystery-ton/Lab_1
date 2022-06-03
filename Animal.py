class Animal:
    __DEFAULT_AMOUNT_OF_HUNGER: int = 3
    __INITIAL_AGE_OF_ANIMALS: int = 0

    def __init__(self):
        self.__type: str = ""
        self.__age: int = 0
        self.__max_age: int = 0
        self.__hunger: int = 0
        self.__food_priority: int = 0
        self.__is_predator: bool = False
        self.__position_x: int = 0
        self.__position_y: int = 0
        self.__symbol: str = ""

    def clone(self, animal: "Animal",) -> "Animal":
        animal.position_x = self.position_x
        animal.position_y = self.position_y
        animal.max_age = self.max_age
        animal.food_priority = self.food_priority
        animal.symbol = self.symbol
        animal.is_predator = self.is_predator
        animal.hunger = self.__DEFAULT_AMOUNT_OF_HUNGER
        animal.age = self.__INITIAL_AGE_OF_ANIMALS
        return animal

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def max_age(self):
        return self.__max_age

    @max_age.setter
    def max_age(self, max_age: int):
        self.__max_age = max_age

    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, hunger: int):
        self.__hunger = hunger

    @property
    def food_priority(self):
        return self.__food_priority

    @food_priority.setter
    def food_priority(self, food_priority: int):
        self.__food_priority = food_priority

    @property
    def is_predator(self):
        return self.__is_predator

    @is_predator.setter
    def is_predator(self, is_predator: bool):
        self.__is_predator = is_predator

    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, position_x: int):
        self.__position_x = position_x

    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, position_y: int):
        self.__position_y = position_y

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol
