# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:13:38 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:13:39 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
        else:
            name = parts[0]
            qty_str = parts[1]

            if name in inventory.keys():
                print(f"Redundant item '{name}' - discarding")
            else:
                try:
                    qty = int(qty_str)
                    inventory[name] = qty
                except ValueError as e:
                    print(f"Quantity error for '{name}': {e}")
        i += 1

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    i = 0
    while i < len(item_list):
        item = item_list[i]
        qty = inventory[item]

        percentage = round((qty / total_qty) * 100, 1)
        print(f"Item {item} represents {percentage}%")
        i += 1

    if len(inventory) > 0:
        most_abundant = item_list[0]
        least_abundant = item_list[0]

        i = 1
        while i < len(item_list):
            item = item_list[i]
            if inventory[item] > inventory[most_abundant]:
                most_abundant = item
            if inventory[item] < inventory[least_abundant]:
                least_abundant = item
            i += 1

        print(
            f"Item most abundant: {most_abundant} with quantity "
            f"{inventory[most_abundant]}"
            )
        print(
            f"Item least abundant: {least_abundant} with quantity "
            f"{inventory[least_abundant]}"
            )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
