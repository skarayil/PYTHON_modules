# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:12:03 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:12:04 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age, growth) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.growth = growth

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self._age} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30, 0.8)

    start_height = plant.height

    print("=== Garden Plant Growth ===")
    plant.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()

    growth = plant.height - start_height
    print(f"Growth this week: {round(growth, 1)}cm")
