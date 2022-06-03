from animals.Predator import Predator
from animals.Omnivorous import Omnivorous
from animals.Herbivore import Herbivore
from animals.impl.Chipmunk import Chipmunk
from animals.impl.Bear import Bear
from animals.impl.Beaver import Beaver
from animals.impl.Fox import Fox
from animals.impl.Hare import Hare
from animals.impl.Hedgehog import Hedgehog
from animals.impl.Moose import Moose
from animals.impl.Mouse import Mouse
from animals.impl.Lynx import Lynx
from animals.impl.Squirrel import Squirrel
from animals.impl.Wolf import Wolf
import pickle
import random


class Simulation:
    __FIELD_SIZE: int = 16
    __MINIMAL_HUNGER_TO_MULTIPLY: int = 2
    __INDENTATION_BETWEEN_TABLES: int = 5
    __ANIMAL_GROUPS_COUNT: int = 3
    __MAX_GRASS_ADDED_TO_FIELD: int = 8
    __NUMBER_OF_CELLS_FILLED_WITH_GRASS: int = 50
    __EMPTY_PARK_AREA_FIELD: str = "*"
    __TIME_TO_UPDATE_GRASS_FIELD: int = 35
    __SERIALIZATION_FILE = "simulation.txt"

    def __init__(self):
        self.__park_area: list = []
        for number_of_row in range(self.__FIELD_SIZE):
            self.__park_area.append([self.__EMPTY_PARK_AREA_FIELD] * self.__FIELD_SIZE)
        self.__animal_list: list = []
        self.__grass_field: list = []
        self.__move_number: int = 0
        self.__data_is_loaded: bool = False
        self.set_of_animals_to_add: list = []
        self.put_animals_to_set: bool = False
        for number_of_row in range(self.__FIELD_SIZE):
            self.__grass_field.append([0] * self.__FIELD_SIZE)



    def __update_grass_field(self) -> None:
        for number_of_cell in range(self.__NUMBER_OF_CELLS_FILLED_WITH_GRASS):
            row = random.randint(0, self.__FIELD_SIZE - 1)
            column = random.randint(0, self.__FIELD_SIZE - 1)
            self.__grass_field[row][column] += random.randint(1, self.__MAX_GRASS_ADDED_TO_FIELD)

    def update_park_area(self) -> None:
        for number_of_row in range(self.__FIELD_SIZE):
            for number_of_column in range(self.__FIELD_SIZE):
                self.__park_area[number_of_row][number_of_column] = self.__EMPTY_PARK_AREA_FIELD
        for animal in self.__animal_list:
            if self.__park_area[animal.position_x][animal.position_y] == self.__EMPTY_PARK_AREA_FIELD:
                self.__park_area[animal.position_x][animal.position_y] = ""
            self.__park_area[animal.position_x][animal.position_y] += animal.symbol

    def load_from_file(self) -> None:
        self.__data_is_loaded = True
        try:
            f = open(self.__SERIALIZATION_FILE, "rb")
            self.__grass_field = pickle.load(f)
            self.__animal_list = pickle.load(f)
        except OSError:
            print("Could not open the file")
        except pickle.UnpicklingError:
            print("Some problems with unpickling an object")
        else:
            f.close()

    def save_to_file(self) -> None:
        try:
            f = open(self.__SERIALIZATION_FILE, "wb")
            pickle.dump(self.__grass_field, f)
            pickle.dump(self.__animal_list, f)
        except pickle.PicklingError:
            print("Some problems with pickling an object")
        else:
            f.close()

    def __initialize(self) -> None:
        self.__data_is_loaded = True
        self.__create_animals()
        self.__set_positions()
        self.__update_grass_field()

    def __create_animals(self) -> None:
        for animal_number in range(self.__ANIMAL_GROUPS_COUNT):
            self.__animal_list.append(Predator("WOLF", 4, 40, "wo"))
            self.__animal_list.append(Predator("FOX", 3, 35, "fo"))
            self.__animal_list.append(Predator("LYNX", 2, 30, "lx"))
            self.__animal_list.append(Omnivorous("CHIPMUNK", 2, 30, "ch"))
            self.__animal_list.append(Omnivorous("HEDGEHOG", 2, 125,  "hd"))
            self.__animal_list.append(Omnivorous("BEAR", 5, 45, "br"))
            self.__animal_list.append(Herbivore("SQUIRREL", 2, 25, "sq"))
            self.__animal_list.append(Herbivore("HARE", 2, 25, "ha"))
            self.__animal_list.append(Herbivore("BEAVER", 3, 30, "bv"))
            self.__animal_list.append(Herbivore("MOOSE", 4, 30, "mo"))
            self.__animal_list.append(Herbivore("MOUSE", 1, 25, "mu"))

    def __set_positions(self) -> None:
        for animal in self.__animal_list:
            animal.position_x = random.randint(0, self.__FIELD_SIZE - 1)
            animal.position_y = random.randint(0, self.__FIELD_SIZE - 1)

    def __restart(self) -> None:
        self.__animal_list.clear()
        self.__grass_field.clear()
        for number_of_row in range(self.__FIELD_SIZE):
            self.__grass_field.append([0] * self.__FIELD_SIZE)
        self.__move_number = 0
        self.__initialize()

    def put_animals_to_set_function(self) -> None:
        self.set_of_animals_to_add.append(Omnivorous("BEAR", 5, 45, "br"))
        self.set_of_animals_to_add.append(Herbivore("BEAVER", 3, 30, "bv"))
        self.set_of_animals_to_add.append(Omnivorous("CHIPMUNK", 2, 30, "ch"))
        self.set_of_animals_to_add.append(Predator("FOX", 3, 35, "fo"))
        self.set_of_animals_to_add.append(Herbivore("HARE", 2, 25, "ha"))
        self.set_of_animals_to_add.append(Omnivorous("HEDGEHOG", 2, 125,  "hd"))
        self.set_of_animals_to_add.append(Predator("LYNX", 2, 30, "lx"))
        self.set_of_animals_to_add.append(Herbivore("MOOSE", 4, 30, "mo"))
        self.set_of_animals_to_add.append(Herbivore("MOUSE", 1, 25, "mu"))
        self.put_animals_to_set = True

    def __choose_animal(self) -> int:
        print("Choose animal you want to add:")
        print("0) - Bear")
        print("1) - Beaver")
        print("2) - Chipmunk")
        print("3) - Fox")
        print("4) - Hare")
        print("5) - Hedgehog")
        print("6) - Lynx")
        print("7) - Moose")
        print("8) - Mouse")
        choice: str = input("Enter a number:")
        get_choice_number: int = int(choice)  ##здесь выбор и возвращаем число , а в эдэнимал пишем ифы
        ##и добавляем животное в список животных в начало(оно само инициализируется, нужно выбрать только координаты )
        return get_choice_number

    def __add_animal(self) -> None:
        animal_to_add=self.__choose_animal()
        if not self.put_animals_to_set:
            self.put_animals_to_set_function()
        self.set_of_animals_to_add[animal_to_add].position_x=random.randint(0,15)
        self.set_of_animals_to_add[animal_to_add].position_y = random.randint(0, 15)
        self.__animal_list.insert(0, self.set_of_animals_to_add[animal_to_add])


    def __get_valid_choice_number(self) -> int:
        while True:
            choice: str = input("Enter a number:")
            try:
                get_choice_number: int = int(choice)
                if 0 > get_choice_number or get_choice_number > 5:
                    print("Entered value " + str(get_choice_number) + " is incorrect")
                    continue
            except ValueError:
                print("Entered value " + choice + " is not a number")
            else:
                break
        return get_choice_number

    def print_menu_and_make_choice(self) -> bool:
        while True:
            print("Choose an action:")
            print("1) - Continue simulation")
            print("2) - Save simulation")
            print("3) - Load simulation")
            print("4) - Restart simulation")
            print("5) - Add animal")
            print("0) - Exit")
            get_choice_number: int = self.__get_valid_choice_number()
            if get_choice_number == 1:
                break
            elif get_choice_number == 2:
                self.save_to_file()
            elif get_choice_number == 3:
                self.load_from_file()
                self.print()
            elif get_choice_number == 4:
                self.__restart()
                self.print()
            elif get_choice_number == 5:
                self.__add_animal()
            else:
                return False
        return True

    def simulate(self) -> None:
        if not self.__data_is_loaded:
            self.__initialize()
        self.print()
        while self.__animal_list:
            if not self.print_menu_and_make_choice():
                return
            self.__move_number += 1
            print("Step #" + str(self.__move_number))
            animal_number = 0
            while animal_number < len(self.__animal_list):
                print(self.__animal_list[animal_number].type + " " + str(
                    self.__animal_list[animal_number].position_x) + ";" + str(
                    self.__animal_list[animal_number].position_y))
                if self.__animal_list[animal_number].hunger > self.__MINIMAL_HUNGER_TO_MULTIPLY:
                    animal_number = self.__multiply(animal_number)

                if self.__animal_list[animal_number].is_predator:
                    self.__try_to_eat_another_animal(animal_number)
                else:
                    self.__try_to_eat_grass(animal_number)

                self.__move(animal_number)
                animal_number += 1

            self.__update_vital_signs()
            if self.__move_number % self.__TIME_TO_UPDATE_GRASS_FIELD == 0:
                self.__update_grass_field()
            self.print()

    def __multiply(self, first_animal_number: int) -> int:
        second_animal_number = 0
        while second_animal_number < len(self.__animal_list):
            if self.__animal_list[first_animal_number] == self.__animal_list[second_animal_number]:
                second_animal_number += 1
                continue
            if type(self.__animal_list[first_animal_number]) != type(self.__animal_list[second_animal_number]):
                second_animal_number += 1
                continue
            if self.__animal_list[first_animal_number].position_x \
                    == self.__animal_list[second_animal_number].position_x \
                    and self.__animal_list[first_animal_number].position_y \
                    == self.__animal_list[second_animal_number].position_y:
                if self.__get_probability(40):
                    print("The " + self.__animal_list[first_animal_number].type + " has multiplied in cell " +
                          str(self.__animal_list[first_animal_number].position_x) + ";" +
                          str(self.__animal_list[first_animal_number].position_y))
                    child_animal = self.__animal_list[first_animal_number].clone(
                        self.__animal_list[first_animal_number].type,self.__animal_list[first_animal_number].food_priority,self.__animal_list[first_animal_number].max_age,self.__animal_list[first_animal_number].symbol)
                    self.__animal_list.insert(0, child_animal)
                    first_animal_number += 1
                    break
            second_animal_number += 1
        return first_animal_number

    def __try_to_eat_another_animal(self, first_animal_number: int) -> None:
        second_animal_number = 0
        while second_animal_number < len(self.__animal_list):
            if self.__animal_list[first_animal_number] == self.__animal_list[second_animal_number]:
                second_animal_number += 1
                continue
            if self.__animal_list[first_animal_number].position_x \
                    == self.__animal_list[second_animal_number].position_x \
                    and self.__animal_list[first_animal_number].position_y \
                    == self.__animal_list[second_animal_number].position_y:
                if self.__animal_list[first_animal_number].food_priority \
                        > self.__animal_list[second_animal_number].food_priority:
                    if self.__get_probability(50):
                        print("The " + self.__animal_list[first_animal_number].type + " has eaten "
                              + self.__animal_list[second_animal_number].type +
                              " in cell " + str(self.__animal_list[first_animal_number].position_x) + ";" +
                              str(self.__animal_list[first_animal_number].position_y))
                        self.__animal_list.remove(self.__animal_list[second_animal_number])
                        self.__animal_list[first_animal_number].hunger += 2
                        break
            second_animal_number += 1

    def __try_to_eat_grass(self, first_animal_number: int) -> None:
        if self.__grass_field[self.__animal_list[first_animal_number].position_x][self.__animal_list[first_animal_number].position_y] > 0:
            self.__grass_field[self.__animal_list[first_animal_number].position_x][self.__animal_list[first_animal_number].position_y] -= 1
            self.__animal_list[first_animal_number].hunger += 1
            print("The " + self.__animal_list[first_animal_number].type + " ate some grass in cell " +
                  str(self.__animal_list[first_animal_number].position_x) + ";" +
                  str(self.__animal_list[first_animal_number].position_y))

    def __update_vital_signs(self) -> None:
        animal_number = 0
        while animal_number < len(self.__animal_list):
            self.__animal_list[animal_number].age += 1
            self.__animal_list[animal_number].hunger -= 1
            if self.__animal_list[animal_number].age == self.__animal_list[animal_number].max_age \
                    or self.__animal_list[animal_number].hunger == 0:
                self.__animal_list.remove(self.__animal_list[animal_number])
                animal_number -= 1
            animal_number += 1
        print("The vital signs of animals have been updated")

    def __get_probability(self, chance: int) -> bool:
        if random.randint(1, 100) > chance:
            return False
        return True

    def print(self) -> None:
        self.update_park_area()
        for i in range(self.__FIELD_SIZE):
            for j in range(self.__FIELD_SIZE):
                print(self.__grass_field[i][j], end=' ')
            print(" " * self.__INDENTATION_BETWEEN_TABLES, end='')
            for j in range(self.__FIELD_SIZE):
                print(self.__park_area[i][j], end=' ')
            print()

    def __move(self, number_of_animal: int) -> None:
        while True:
            new_position_x = self.__animal_list[number_of_animal].position_x
            new_position_y = self.__animal_list[number_of_animal].position_y

            if random.choice([True, False]):
                new_position_x += random.choice([-1, 1])
            else:
                new_position_y += random.choice([-1, 1])
            if 0 <= new_position_x < self.__FIELD_SIZE:
                if 0 <= new_position_y < self.__FIELD_SIZE:
                    break

        print("The " + self.__animal_list[number_of_animal].type + " has moved " + str(
            self.__animal_list[number_of_animal].position_x) + ";" + str(
            self.__animal_list[number_of_animal].position_y) + "->" + str(new_position_x) + ";" + str(new_position_y))

        self.__animal_list[number_of_animal].position_x = new_position_x
        self.__animal_list[number_of_animal].position_y = new_position_y
