# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:12:20 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:12:21 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0
            self._shade = 0

        def record_grow(self) -> None:
            self._grow += 1

        def record_age(self) -> None:
            self._age += 1

        def record_show(self) -> None:
            self._show += 1

        def record_shade(self) -> None:
            self._shade += 1

        def get_stats(self) -> dict:
            return {
                "grow": self._grow,
                "age": self._age,
                "show": self._show,
            }

    def __init__(self, name, height, age) -> None:
        self.name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0
        self._stats = self._Stats()

    @staticmethod
    def is_older_than_a_year(age_in_days: int) -> bool:
        return age_in_days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

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

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> dict:
        return self._stats.get_stats()

    def age(self, amount: int = 1) -> None:
        self._stats.record_age()
        self._age += amount

    def grow(self, amount: float = 1.0) -> None:
        self._stats.record_grow()
        self._height += amount

    def show(self) -> None:
        self._stats.record_show()
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
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def record_shade(self) -> None:
            self._shade += 1

        def get_stats(self) -> dict:
            stats = super().get_stats()
            stats["shade"] = self._shade
            return stats

    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self._stats = self._TreeStats()
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.record_shade()
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

    def grow(self, amount: float = 1.0) -> None:
        super().grow(amount)
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    stats = plant.get_stats()
    print(
        f"Stats: {stats['grow']} grow, "
        f"{stats['age']} age, "
        f"{stats['show']} show"
    )
    if "shade" in stats:
        print(f" {stats['shade']} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_a_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_a_year(400)}"
    )

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_statistics(anon)
