# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:12:12 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:12:13 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        if height >= 0:
            self._height = height
        else:
            self._height = 0
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

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print(
        f"Plant created: "
        f"{plant.name}: {plant._height}cm, {plant._age} days old"
    )
    print("")
    plant.set_height(25)
    plant.set_age(30)
    print("")
    plant.set_height(-5)
    plant.set_age(-10)
    print("")
    print(
        f"Current state: {plant.name}: "
        f"{plant.get_height()}cm, {plant.get_age()} days old"
    )
