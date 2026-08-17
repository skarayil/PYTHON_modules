# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:12:53 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:12:54 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants_list: list[str]) -> None:
    print("Opening watering system")

    try:
        for plant in plants_list:
            water_plant(plant)

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(valid_plants)

    print("\nTesting invalid plants...")
    invalid_plants = ["Tomato", "lettuce"]
    test_watering_system(invalid_plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
