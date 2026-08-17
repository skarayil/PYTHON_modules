# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:12:16 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:12:17 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")

    def set_height(self, h) -> None:
        if h < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = h
            print(f"Height updated: {h}cm")

    def set_age(self, a) -> None:
        if a < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = a
            print(f"Age updated: {a} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def age(self) -> None:
        self._age += 1

    def grow(self, amount=1) -> None:
        self._height += amount

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount=1) -> None:
        super().grow(amount)
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    veg = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Flower")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()

    print("\n=== Tree")
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    veg.show()
    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        veg.grow(2.1)
        veg.age()

    veg.show()
